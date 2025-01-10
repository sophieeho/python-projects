#sophie
import random
points = 0
print("Welcome to the multiplication game!")#this introduces the game
print("Answer the math problems to gain points")
ans = input("normal(n) or endless(end)?")#the game asks which mode they player wants to be in
if ans == "n":#if they chose normal mode it asks hard or easy difficulty
    ans = input("hard(h) or easy (e)?")
    if ans == "h":#if they chose hard then the randomized numbers that are chosen for the equations are between 50 and 100
        questions = int(input("input the number of questions you want to answer"))
        for i in range(questions):
            x = random.randint(50,100)
            y = random.randint(50,100)
            guess = input("what is the solution for the equation " + str(x) + " times " + str(y))
            if guess == str(x*y):
                points = points + 1
                print("you are correct! good job!")
                print("you have " + str(points) + " points")#if they get it correct, they get a point
            else:
                print("you are incorrect")
    print("your final score is " + str(points) + " points")#once they are done their final score is displayed
    if ans == "e":#if they chose easy then the randomized numbers that are chosen for the equations are between 0 and 10
        questions = int(input("input the number of questions you want to answer"))#this asks the player how many questions they want to answer
        for i in range(questions):
            x = random.randint(0,10)
            y = random.randint(0,10)
            guess = input("what is the solution for the equation " + str(x) + " times " + str(y))
            if guess == str(x*y):
                points = points + 1
                print("you are correct! good job!")
                print("you have " + str(points) + " points")
            else:
                print("you are incorrect")
    endprint("your final score is " + str(points) + " points")
if ans == "end":#this is endless mode
        ans = input("hard(h) or easy (e)?")#after endless mode ask if it is hard or easy
        if ans == "h":
            while True:
                questions = print("you are in endless mode you have endless questions")
                x = random.randint(50,100)
                y = random.randint(50,100)
                guess = input("what is the solution for the equation " + str(x) + " times " + str(y))
                if guess == str(x*y):
                    points = points + 1
                    print("you are correct! good job!")
                    print("you have " + str(points) + " points")
                else:
                    print("you are incorrect")
                ans1 = input("would you like to quit?")#this is asked after every endless question as an option to end
                if ans1 == "yes":
                    break
        print("your final score is " + str(points) + " points")
        if ans == "e":
            while True:
                questions = print("you are in endless mode you have endless questions")
                x = random.randint(0,10)
                y = random.randint(0,10)
                guess = input("what is the solution for the equation " + str(x) + " times " + str(y))
                if guess == str(x*y):
                        points = points + 1
                        print("you are correct! good job!")
                        print("you have " + str(points) + " points")
                else:
                    print("you are incorrect")
                ans1 = input("would you like to quit?")#this allows the person to quit from endless mode
                if ans1 == "yes":
                    break
        print("your final score is " + str(points) + " points")


