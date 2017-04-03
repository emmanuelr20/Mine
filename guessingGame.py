from random import random
from math import floor
ask=1
while ask != 0:
    print("I am looking for a number between 0 and 9??")
    answer=random()*100//10
    numOfTries=3
    while numOfTries >0:
        guess=int(input("Enter guess: "))
        if guess==answer:
            print("You guessed correctly!!!\nAnswer ={}".format(answer))
            numOfTries=3
        elif guess>answer:
            print("Incorrect Answer Try again!!!\nyour guess is greater than the answer!")
            numOfTries-=1
        else:
            print("Incorrect Answer Try again!!!\nyour guess is less than the answer!")
            numOfTries-=1
    ask=input("press (0) to exit or anykey to continue: ")
    print("\n")
