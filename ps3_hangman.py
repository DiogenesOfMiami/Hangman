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

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#OldSetup
#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
#wordlist = loadWords()

#NewSetup
#secretWord = chooseWord(wordlist).lower()
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

#Drawing the noose
noose = turtle.Turtle()
noose.width(10)
noose.hideturtle()
noose.color("darkgreen")
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
noose.goto(0,150)

window.update()
guessedLetter = turtle.textinput(" ", 'Input:')

# --- Main ---
while guessedLetter.lower() == 'new':
    lettersGuessed = []
    secretWord = "test"                                                                 #REMOVE AFTER TESTING
    guessesLeft = 8

    while guessesLeft > 0:
        # Window Updating
        bMessage = 'Available letters: ' + getAvailableLetters(lettersGuessed)
        window.update()
        bText.clear()
        bText.write(bMessage, align="center", font=(font))
        tText.clear()
        tText.write(tMessage, align="center", font=(font))
        
        # Guessing
        guessedLetter = turtle.textinput(" ", 'Please guess a letter:')

        if guessedLetter in lettersGuessed:
            tMessage = "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed) # PROGRESS
        else:
            lettersGuessed.append(guessedLetter)

        if guessedLetter in secretWord:
          tMessage = 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
          if isWordGuessed(secretWord, lettersGuessed):
            tMessage = 'Congratulations, you won!'
            bMessage = "Input 'new' for a new game or 'quit' to quit."
        else:
          guessesLeft -= 1
          tMessage = 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
          
          if guessesLeft == 0:
            tMessage = 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'