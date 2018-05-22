import random
HANGMANPICS = ['''

 +---+
 |   |
     |
     |
     |
     |
 =========''', '''

 +---+
 |   |
 o   |
     |
     |
     |
 =========''', '''

 +---+
 |   |
 o   |
 |   |
     |
     |
 =========''', '''

 +---+
 |   |
 o   |
/|   |
     |
     |
 ========''', '''
 
 +---+
 |   |
 o   |
/|\  |
     |
     |
 ========''', '''
 
 +---+
 |   |
 o   |
/|\  |
/    |
     |
 ========''', '''
 
 +---+
 |   |
 o   |
/|\  |
/ \  |
     |
 ========''']
words = 'ant baboon badger bat bear baeaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk linon lizard llama mole monkey mouse moose mole newt otter owl panda parrot sloth snake spider stork  swan tiger toad  trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
def  displayBoard(HANGMANPICS, missedLetter, correctLetter, secretWord):
    print(HANGMANPICS[len(missedLetter)])
    print()
    
    print('Missed letters:', end='')
    for letter in missedLetter:
        print(letter, end='')
    print()
    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetter:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end='')
    print()
    
def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a simple letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER.")
        else:
            return guess
def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

print('HANGMAN')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters,secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllletters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllletters = False
                break
        if foundAllletters:
            print("yes! The secret word is " + secretWord + "! You have won!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print("You have run out of guesses! \n After" + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guesses, the word was " + secretWord + " ")
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters =''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break 
        
        