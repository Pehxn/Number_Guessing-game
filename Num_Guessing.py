#random module
import random

#welcome
print("Hiiii!! Welcome to Number Guessing Game")

#user inputs assign
x = int(input("What is the lower limit ")) #also x.isdigit can be used to check whether it is a number.
y = int(input("What is the upper limit "))

r = random.randrange(x,y) #r=random number
#print("Random Number is "+ str(r))

while True:
    guess = int(input("make a guess "))

    if guess == r:
        print("Congratzz!! U Got It right ")
        break

    else:
        if r>guess:
            print("U Got it WRONG... (try Higher XD)")

        else:
            print("U Got it WRONG... (try Lower XD)")
        continue
