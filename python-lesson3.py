import random
number_of_guess = random.randint(1,10)
guess = None

while guess != number_of_guess:
    guess = int(input("Guess a number beetwen 1 and 10:"))
    if guess < number_of_guess:
        print("Too low,try again")
    elif guess > number_of_guess:
        print("Too high, try again")
    else:
        print("Congrats, you guessed the number!")
