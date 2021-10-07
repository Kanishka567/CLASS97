import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess a number (between 1 and 9):") 
while chances < 5:
    guess=int(input("enter your guess :->"))
    if guess ==number:
        print("CONGRATULATIONS!YOU WON!!")
        break
    elif guess < number:
        print("YOUR GUESS WAS TOO LOW:GUESS A NUMBER HIGHER THAN!",guess)
    else:
        print("YOUR GUESS WAS TOO HIGH!: GUESS A NUMBER LOWER THAN!",guess)  
    chances+=1
if not chances < 5:
    print("YOU LOSE!THE NUMBER IS",number)          