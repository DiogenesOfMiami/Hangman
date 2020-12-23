from random import choice
from turtle import Turtle, Screen, textinput, numinput
from easy_draw_turtle import EasyDrawTurtle
from string import ascii_lowercase
import json

class GameGui(Turtle):
    ''' Object that encapsulates the main window and all its underlying panels.'''

    # Declare prompts for all the menus
    START_PROMPT = "Input 'new' for a new game or 'quit' to quit."
    GUESS_PROMPT = "Guess a letter:"
    DIFFICULTY_PROMPT = 'Select a difficulty level: ( 1:EASY | 2:MODERATE | 3:HARD )'

    def __init__(self,word_list_path = 'words.txt'):
        
        Turtle.__init__(self)

        # Constant declarations
        self.version = "v0.2"

        # Get a string with all words
        with open(file=word_list_path,mode='r') as word_list_file:
            word_dump = word_list_file.read()
        
        # Split the string into a word list by spaces
        self.wordlist = word_dump.split(sep=' ')

        # Build a list of remaining letters
        self.remaining_options = list(ascii_lowercase)
        
    def create_window(self):
        ''' Perform all preliminary configuration steps to load up the Gui window such as setting the title.'''

        # Create the main window
        self.window = Screen()
        self.window.title = self.game_title = f"Cassy's Hangman {self.version}"
        self.window.bgcolor('black')
        self.window.setup()
        self.window.tracer(0)

        # Create all subobjects of the window including the two panels, the man and the noose.
        self.top_panel = Panel(start=(0,-260), initial_message=f"Welcome to {self.game_title}!") 
        self.bottom_panel = Panel(start=(0,-320),initial_message=self.START_PROMPT) 
        self.outcome_panel = Panel(start=(0,260),initial_message='')
        self.noose = Noose(parent=self,color="darkgreen",width=10,hide_turtle=True)
        self.man = Man(parent=self,color="darkgreen",width=10,hide_turtle=True)

    def start_menu(self):
        ''' Display the game's start menu and prompt the user wether they wish to play a new game or quit.'''

        # Display a persistent prompt to the user
        while 1 == 1:

            # Get the user's choice.
            choice = textinput('Wanna play?',self.START_PROMPT)

            # If the choice is valid then break out of the infinite loop otherwise let the user know and repeat.
            if choice in ['new','quit']: 
                break
            else:
                self.bottom_panel.display_message(f'"{choice}" is not a valid input. Try again. ')

        # If the user chose to play then run the game otherwise close the window
        if choice == 'new': 
            self.difficulty_menu()
        else:
            self.window.bye()

    def difficulty_menu(self):
        ''' Display a menu to prompt the user what difficulty level they wish to play.'''

        # Lambda functions defining the word filters for each difficulty.
        word_filters = {
            1: lambda word: len(word)<=5, # easy
            2: lambda word: 5<len(word)<=7, # moderate
            3: lambda word: 7<len(word) # hard
        }

        # Get the user's choice.
        choice = numinput(title='Dificulty level',prompt=self.DIFFICULTY_PROMPT,minval=1,maxval=3)

        # Filter the wordlist based on the user's choice
        word_filter = word_filters[int(choice)]
        self.wordlist = [word for word in filter(word_filter,self.wordlist)]

        # Begin the game
        self.play_game()
        self.window.mainloop()

    def play_game(self):
        ''' Run the main logic of the game.'''

        # Clear the bottom panel to start the game
        self.bottom_panel.clear()

        # Select a random word from the list and make a list to store guesses.
        word = choice(self.wordlist)
        guesses = []
        
        # While the man is not dead.
        while not self.man.dead:

            # Adjust the word display to show which letters have been guessed correctly.
            word_display = "".join([ f' {letter}' if letter in guesses else ' _' for letter in word])
            self.top_panel.display_message(f'Word: {word_display}')

            # If the whole word is guessed then exit the loop.
            if word_display.replace(' ','') == word: break
            
            # Ask the user for a letter and add it to the guess list
            guess = textinput('You can do this!', f'Remaining options: {self.remaining_options}\n{self.GUESS_PROMPT}').lower()
            guesses +=[guess]

            # If the guess is part of the remaining options
            if guess in self.remaining_options:

                # Remove it from the list of remaining options and determine if it was a success.
                self.remaining_options.remove(guess)
                success = guess in word

                # Give a response prompt besed on wether the user guessed correctly.
                response_prompt = f'"{guess}" IS A GOOD GUESS! CONGRATULATIONS!' if success else f'OHOH! Wrong guess. "{guess}" is not in the word.'
                self.bottom_panel.display_message(response_prompt)
                
                # Draw a limb if the user guessed incorrectly.
                if not success: self.man.draw_limb()

            # Otherwise (if the guess was not one of the remaining options or is invalid) then
            else:

                # Inform the user
                self.bottom_panel.display_message(f'"{guess}" was already picked or is invalid.')

        # Display the outcome prompt and the hidden word.
        self.outcome_panel.display_message('YOU WIN!' if success else 'YOU LOSE!')
        self.top_panel.display_message(f'The word was: {word}')
        self.bottom_panel.clear()

class Panel(Turtle):
    ''' Object that encapsulates a small text region on the main window. '''

    def __init__(self, start ,initial_message):
        ''' Create and configure the panel object at a specific start placement.'''
        Turtle.__init__(self)
        self.font = ("Share Tech Mono", 24, "normal")
        self.speed(0)
        self.color("darkgreen")
        self.penup()
        self.hideturtle()
        self.goto(start)
        self.write(initial_message, align="center", font=self.font)

    def display_message(self,message):
        ''' Replace the current message with a new one.'''
        self.clear()
        self.write(message,align='center',font=self.font)
            
class Noose(EasyDrawTurtle):
    ''' Class that encapsulates the noose object on the screen.'''

    def draw(self):
        ''' Draw the noose.'''

        # Get the strokes as a json object
        with open(file='noose.json',mode='r') as json_file: 
            strokes = json.load(json_file)
        
        # Draw them all
        self.draw_strokes(strokes)
        self.parent.window.update()

class Man(EasyDrawTurtle):
    ''' Class that encapsulates the man object on the screen. Tracks lives as well.'''

    @property
    def dead(self): 
        ''' Return True if the man is completely drawn otherwise False.'''
        return len(self.strokes) == 0

    def __init__(self,parent,color,width,hide_turtle):
        ''' Import the man's strokes from json file.'''

        EasyDrawTurtle.__init__(self,parent,color,width,hide_turtle)
        
        # Get the strokes as a json object
        with open(file='man.json',mode='r') as json_file: 
            self.strokes = json.load(json_file)

    def draw_limb(self):
        ''' Draw a single limb and remove a life.'''
        stroke = self.strokes.pop(0)
        self.draw_stroke(stroke['start'],stroke['stroke_method_str'],stroke['parameters'])
        self.parent.window.update()

if __name__ == '__main__':
    
    UI = GameGui()
    UI.create_window()
    UI.noose.draw()
    UI.start_menu()
    
    