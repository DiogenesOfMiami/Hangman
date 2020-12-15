# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import turtle

WORDLIST_FILENAME = "E:/My Documents/Programming/Projects/Hangman/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWordList = list(secretWord)
    return all(elem in lettersGuessed for elem in secretWordList)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    secretWordList = list(secretWord)
    lettersGuessedList = list(set(lettersGuessed))
    for letter in secretWordList:
        if letter not in lettersGuessedList:
            secretWordList[secretWordList.index(letter)] = '_ '
    return ''.join(map(str, secretWordList))



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    import string
    alphaList = list(string.ascii_lowercase)
    for char in lettersGuessed:
        if char in alphaList:
            alphaList.remove(char)
    return ''.join(map(str, alphaList)) 
    

# def hangman(secretWord):
#     '''
#     secretWord: string, the secret word to guess.

#     Starts up an interactive game of Hangman.

#     * At the start of the game, let the user know how many 
#       letters the secretWord contains.

#     * Ask the user to supply one guess (i.e. letter) per round.

#     * The user should receive feedback immediately after each guess 
#       about whether their guess appears in the computers word.

#     * After each round, you should also display to the user the 
#       partially guessed word so far, as well as letters that the 
#       user has not yet guessed.

#     Follows the other limitations detailed in the problem write-up.
#     '''
#     guessesLeft = 8
#     lettersGuessed = []

#     print('Welcome to the game, Hangman!')
#     print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
#     print('-------------')
#     while guessesLeft >= 1:
#       print('You have ' + str(guessesLeft) + ' guesses left.')
#       print('Available letters: ' + getAvailableLetters(lettersGuessed))
#       guessedLetter = input('Please guess a letter: ')
#       if guessedLetter in lettersGuessed:
#         print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
#         print('-------------')
#       else:
#         lettersGuessed.append(guessedLetter)
#         if guessedLetter in secretWord:
#           print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
#           print('-------------')
#           if isWordGuessed(secretWord, lettersGuessed):
#             print('Congratulations, you won!')
#             break
#         else:
#           guessesLeft -= 1
#           print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
#           print('-------------')
#           if guessesLeft == 0:
#             print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
#     input()

#OldSetup
#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)

#-----NewSetup-----
#wordlist = loadWords()
version = "v0.1"
gameTitle = "Cassy's Hangman "+version
window = turtle.Screen()
window.title(gameTitle)
window.bgcolor("black")
window.setup()
window.tracer(0)
tMessage = "Welcome to "+gameTitle+"!"
bMessage = "Input 'new' for a new game or 'quit' to quit."
font = ("Share Tech Mono", 24, "normal")

#TopText
tText = turtle.Turtle()
tText.speed(0)
tText.color("darkgreen")
tText.penup()
tText.hideturtle()
tText.goto(0,-260)
tText.write(tMessage, align="center", font=(font))

#BottomText
bText = turtle.Turtle()
bText.speed(0)
bText.color("darkgreen")
bText.penup()
bText.hideturtle()
bText.goto(0,-290)
bText.write(bMessage, align="center", font=(font))

#Creating the noose
noose = turtle.Turtle()
noose.width(10)
noose.hideturtle()
noose.color("darkgreen")
noose.penup()

#Drawing the noose
def drawNoose():
    noose.penup()
    noose.goto(-200,-200)
    noose.pendown()
    noose.goto(200,-200)
    noose.goto(150,-200)
    noose.goto(100,-150)
    noose.goto(50,-200)
    noose.penup()
    noose.goto(100,-200)
    noose.pendown()
    noose.goto(100,200)
    noose.goto(0,200)
    noose.penup()
    window.update()

#Creating the man
man = turtle.Turtle()
man.width(10)
man.hideturtle()
man.color("darkgreen")
man.penup()

#Drawing the man
def newLimb(limbs):
    if limbs == 6: #Draw rope
        man.goto(0,200)
        man.pendown()
        man.goto(0,150)
        man.penup()

    elif limbs == 5: #Draw head
        man.goto(0,100)
        man.pendown()
        man.circle(25)
        man.penup()        

    elif limbs == 4: #Draw body
        man.goto(0,100)
        man.pendown()
        man.goto(0,25)
        man.penup()
    
    elif limbs == 3: #Draw left leg
        man.goto(0,25)
        man.pendown()
        man.goto(-30,-40)
        man.penup()
    
    elif limbs == 2: #Draw right leg
        man.goto(0,25)
        man.pendown()
        man.goto(30,-40)
        man.penup()

    elif limbs == 1: #Draw left arm
        man.goto(0,75)
        man.pendown()
        man.goto(-30,15)
        man.penup()

    elif limbs == 0: #Draw right arm
        man.goto(0,75)
        man.pendown()
        man.goto(30,15)
        man.penup()

    

guessedLetterRaw = turtle.textinput("Input", ' ')
guessedLetter = guessedLetterRaw.lower()

# --- Main ---
while guessedLetter == 'new':
    drawNoose()
    man.clear()
    lettersGuessed = []
    secretWord = "test"                                                                 #REMOVE AFTER TESTING
    #secretWord = chooseWord(wordlist).lower()                                          #UNCOMMENT AFTER TESTING
    guessesLeft = 7
    tText.clear()
    bText.clear()
    tMessage = "Welcome to "+gameTitle+"!"

    while guessesLeft > 0:
        # Window Updating
        bMessage = 'Remaining letters: ' + getAvailableLetters(lettersGuessed)
        window.update()
        bText.clear()
        bText.write(bMessage, align="center", font=(font))
        tText.clear()
        tText.write(tMessage, align="center", font=(font))
        
        # Guessing
        guessedLetter = turtle.textinput("Input", 'Please guess a letter:')

        if guessedLetter in lettersGuessed:
            tMessage = "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed) 
        else:
            lettersGuessed.append(guessedLetter)

            if guessedLetter in secretWord:
                if isWordGuessed(secretWord, lettersGuessed):
                    noose.clear()
                    tText.clear()
                    tMessage = 'Congratulations, you won!'
                    tText.write(tMessage, align="center", font=(font))
                    guessedLetter = turtle.textinput("Input", "Input 'new' for a new game or 'quit' to quit.")
                    break
                else:
                    tMessage = 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
            else:
                guessesLeft -= 1
                newLimb(guessesLeft)
                if guessesLeft < 1:
                    break
                else:
                    tMessage = 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)

    tText.clear()      
    tMessage = 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
    tText.write(tMessage, align="center", font=(font))
    guessedLetter = turtle.textinput("Input", "Input 'new' for a new game or 'quit' to quit.")

            