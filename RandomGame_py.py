import random as r
import pandas as pd

def guess_func(x):
    guess = int(0)
    random_number = r.randint(1,x)
    while guess != random_number :
        
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
        except:
            pass

        if type(guess) != int or guess > x or guess < 1:
            print(f"you must enter a numberical value between 1 and {x}:")
        else:
            print("Sorry Guess again :(")
        
    
guess_func(11)