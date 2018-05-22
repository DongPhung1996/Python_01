import random
print("I will flip a coin 1000 times. Guess how many time it will come up heads. (Press enter to begin)")
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1
    
    if flips == 900:
        print("900 flips and there have been " + str(heads) + " heads.")
    if flips == 100:
        print("At 100 tosses, heads has come up " + str(heads) + " times so far")
    if flips == 500:
        print("Half way done, and heads has come up " + str(heads) + " times!")
print()
print("Out of 100 coin tosses, heads came up " + str(heads) + " time!")
print("Were you close?")