# import random function to pick a random word
from random import choice

# Returns a random word
def getRandomWord():
    words = "python program keyboard mouse procedure function subprogram"

    # Following picks a random word from string
    # The mechanism is discussed in more detail later
    word = choice(words.split())

    return word

# Returns the word to be built, i.e. a word consisting of
# correct number of hyphens
def getBuiltWord(correctWord):
    return "-" * len(correctWord)


# Queries the user for a single character and returns it
def queryAnswer():
    c = ""
    while len(c) != 1:
        c = input("Give a character: ")
        if len(c) != 1:
            print ("Give a single character!")
    return c

# Returns true, if the given character can be found in given word
def charInWord(word, character):
    return word.find(character) > -1

# Inserts given character into correct places in the word
def insertChar(correctWord, builtWord, character):
    # Iterate through the words
    for i in range(len(correctWord)):
        # check if char to be inserted
        # and not yet inserted
        if correctWord[i] == character and builtWord[i] == "-":
            # replace with char in built word
            builtWord = builtWord[0:i] + character + builtWord[i + 1: ]

    return builtWord

# Draws the hanging man based on the number of incorrect guesses
# To keep the program simpler, only four alternatives are provided
def drawHangingMan(incorrectGuesses):
    if incorrectGuesses >= 1:
        print (" +--- ")
        print (" |")
        print (" o")
    if incorrectGuesses >= 2:
        print ("/|\\")
    if incorrectGuesses >= 3:
        print (" |")
    if incorrectGuesses == 4:
        print ("/ \\")


# Main program
correctWord = getRandomWord()
builtWord = getBuiltWord(correctWord)
incorrectGuesses = 0

# Loop until user guesses the word or four incorrect tries are made
while incorrectGuesses < 4 and builtWord != correctWord:
    # output current word and query for letter
    print (builtWord)
    c = queryAnswer()
    if charInWord(correctWord, c):
        builtWord = insertChar(correctWord, builtWord, c)
    else:
        incorrectGuesses = incorrectGuesses + 1
    drawHangingMan(incorrectGuesses)
    print ("\n")

# Finally output the 
print ("The word was", correctWord)
if builtWord == correctWord:
    print ("You won!")
else:
    print ("You lost!")
        
        
    

