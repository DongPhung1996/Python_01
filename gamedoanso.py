import random

guessTaken = 0

number = random.randint(1,20)

print("xin chao! Ban ten la gi?")

myName = input()

print("Chao " + myName + "! ban hay doan so ma toi dang nghi")

while guessTaken < 6:
    print("Moi ban doan so:")
    guess = input()
    guess = int(guess)
    guessTaken += 1
    if guess < number:
        print("ban doan thap hon roi")
    elif guess > number:
        print("Ban doan cao hon roi")
    else:
        break
if guess == number:
    print("ban da doan dung! Voi " + str(guessTaken) + " lan doan")
else:
    print("ban doan sai roi. So minh dang nghi la: " + str(number))