import random

guessTaken = 0

number = random.randint(1, 20)

print("hello! \n What is your name?")
myName = input()

while guessTaken < 8:
    print("Hey " + myName + "! I am thinking a number between 1 and 20")
    guess = input()
    guess = int(guess)
    
    guessTaken += 1
    
    if guess < number:
        print("Your number is low! Please continue!")
    elif guess > number:
        print("Your number is high! Please continue!")
    else: break
    
if guess == number:
    print("Well" + myName + "! Guess counts:" + str(guessTaken))
else:
    print("opp, you lose. I am thinking number is " + str(number))
        