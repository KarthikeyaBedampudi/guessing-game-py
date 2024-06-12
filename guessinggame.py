import random
import time

def intro():
    print("May I ask you for your name?")
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name

def pick(number, name):
    guessesTaken = 0
    while guessesTaken < 6:
        enter = input("Guess: ")
        try:
            guess = int(enter)

            if 1 <= guess <= 200:
                guessesTaken += 1
                if guess < number:
                    print("The guess of the number that you have entered is too low")
                elif guess > number:
                    print("The guess of the number that you have entered is too high")
                else:
                    break
                if guessesTaken < 6:
                    print("Try Again!")
            else:
                print("Silly Goose! That number isn't in the range!")
                print("Please enter a number between 1 and 200")

        except ValueError:
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:
        print(f'Good job, {name}! You guessed my number in {guessesTaken} guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(number))

def main():
    playagain = "yes"
    while playagain.lower() in ["yes", "y"]:
        number = random.randint(1, 200)
        name = intro()
        pick(number, name)
        print("Do you want to play again?")
        playagain = input()

if _name_ == "_main_":
    main()
