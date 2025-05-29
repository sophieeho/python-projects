#sophie
#init
import random
import time
global question
#function
response = ["no sorry", "maybe next time", "think harder and try again", "sorry but definitely not", "yes!", "of course", "possibly...", "per chance", "absolutely not.", "yes yes yes", "absolutely!", "i don't know try again", "no.", "my sources say no", "most likely", "signs point to yes"]
def magic_guesser():
    while True:
        guess = input("Ask a yes or no question")
        if guess.endswith("?"):
            time.sleep(2)
            print("Shaking...")
            time.sleep(2)
            print(random.choice(response))
            question = input("would you like to ask another question yes(y) or no(n)?")
            if question == "y":
                print("game beginning again")
            if question == "n":
                print("thanks for playing")
                break
        else:
            print("no question was asked, please ask again with a question mark.")
            break



#main
magic_guesser()

