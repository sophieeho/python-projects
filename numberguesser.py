#sophie
#guessing game
import random
print("Welcome to the number guesser game!")
print("Guess the chosen number between 1 and 10 and win!")#this is the intro to the game
guess = int(input("Enter Number"))#this asks the player to choose a number
secret = random.randint(0,10)#this randomizes the number
if guess == secret:#if guess is right then it prints the sentence below
        print("You have guessed the right number!")
else:#this is for if guess is wrong
        print("You have not guessed the right number, try again.")
if guess<secret:#if guess is less than secret number it allows you to try again and gives the option for yes or no
    print("Your guess was too low, would you like a second guess?")
    ans = input("Yes(Y) or No (N)")
    if ans == "Y":
        print("Welcome to the number guesser game!")
        print("Guess the chosen number between 1 and 10 and win!")
        guess = int(input("Enter Number"))
        if guess == secret:
                print("You have guessed the right number!")
        if ans == "N":
                print("Thanks for playing!")
        if guess<secret:
                print("Your guess was too low, The correct number is " + str(secret) + " would you like to start over?")
                ans = input("Yes(Y) or No (N)")
                if ans == "Y":
                        print("Welcome to the number guesser game!")
                        print("Guess the chosen number between 1 and 10 and win!")
                        guess = int(input("Enter Number"))
                        if guess == secret:
                                print("You have guessed the right number!")
                        if ans == "N":
                                print("Thanks for playing!")
if guess>secret:#if guess is more than secret number it allows you to try again and gives the option for yes or no
    print("Your guess was too high, would you like a second guess?")
    ans = input("Yes(Y) or No (N)")
    if ans == "Y":
        print("Welcome to the number guesser game!")
        print("Guess the chosen number between 1 and 10 and win!")
        guess = int(input("Enter Number"))
        if guess == secret:
                print("You have guessed the right number!")
        if ans == "N":
                print("Thanks for playing!")
        if guess>secret:
                print("Your guess was too high, The correct number is " + str(secret) + " would you like to start over?")
                ans = input("Yes(Y) or No (N)")
                if ans == "Y":
                        print("Welcome to the number guesser game!")
                        print("Guess the chosen number between 1 and 10 and win!")
                        guess = int(input("Enter Number"))
                        if guess == secret:
                                print("You have guessed the right number!")
                        if ans == "N":
                                print("Thanks for playing!")
