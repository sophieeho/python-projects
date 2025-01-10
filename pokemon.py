#Init
pokemon_level = 0
pokemon_name = "Eevee" #this is your pokemon
day = 1
wins = 0
losses = 0
import random
#functions
def train():#this is the function that executes basic training for the pokemon and as the pokemon trains, the pokemon level goes up
    print("Your Pokemon did 10 pushups")
    global pokemon_level
    pokemon_level = pokemon_level + 1
    print("your pokemon's level is " + str(pokemon_level))
def gymbattle(): #this is the function for the gym battle, the poke,on plays against another pokemon and everytime you win, the win count goes up as well as the pokemon level
    global pokemon_level
    global wins
    global losses
    outcome = random.randint(1,2) #50% chance to win or lose
    if outcome == 1:
        print("You have won the battle! Good work! You went up two levels!")
        pokemon_level = pokemon_level + 2
        print("your pokemon's level is " + str(pokemon_level))
        wins = wins + 1
    else:
        print("You have been defeated. You remain at the same level. Try again later.")
        losses = losses + 1
def rest(): #this is the rest checkpoint, where the player is able to see the pokemons stats
    #pokemon name and level
    print("Your Pokemon's name is " + (pokemon_name))
    print("Your Pokemon's level is " + str(pokemon_level))
    print("You have " + str(wins) + " wins and " + str(losses) + " losses")
def quit(): #this is the function that enables quitting the game
    print("Thanks for playing, hope you enjoyed!")
def evolve():#this is the function that works to evolve the pokemon once it reaches certain levels
    if pokemon_level >= 5:
        global pokemon_name
        pokemon_name = "Sylveon"
        print("Your Pokemon evovled into a Sylveon!")
    if pokemon_level >= 10:
        pokemon_name = "Leafeon"
        print("Your Pokemon evolved into a Leafeon!")
def finalboss_battle(): #this is the final boss battle, it is the final battle that is worth 5 points if you win
    global pokemon_level
    global wins
    global losses
    if pokemon_level >= 50:
        outcome = random.randint(1,2)
        if outcome == 1:
            print("You have won the final battle! Good work you have completed your journey!")
            pokemon_level = pokemon_level + 5
            print("your pokemon's level is " + str(pokemon_level))
            wins = wins + 1
        else:
            print("You have been defeated. Your journey has come to an end")
            losses = losses + 1
    else:
        print("You cannot challenge the final boss, your pokemon is not a high enough level")
#main
print("welcome to pokemon evolution")
while True:
    print("choose an activity for day: " + str(day))
    print("""1.train
    2.gym battle
    3.rest(display info)
    4.final battle
    5.Quit
    """)
    activity = int(input("Activity for the day: "))
    if activity == 1:
        train()
        day = day + 1
        evolve()
    elif activity == 2:
            gymbattle()
            day = day + 1
            evolve()
    elif activity == 3:
            rest()
    elif activity== 4:
            finalboss_battle()
    elif activity==5:
            quit()
