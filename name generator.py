#Sophie Ho
#Which Disney Princess are You?
print("Welcome to Disney Princess Name 2000")
print("Answer the questions to find out which Disney Princess you are")
ans = input("winter(w) or fall (f)?")#this asks the audience whether they like winter or fall
if ans =="w": #this means if they choose winter they get asked dog or fish?
    ans = input("dog (d) or fish (f)?")
    if ans == "d":#if they choose dog, they get asked purple or green?
        ans = input("purple(p) or green(g)?")
        if ans  == "p":#if they choose purple they are rapunzel
            print("You are Rapunzel")
        else:#if they choose green they are tiana
            print("You are Tiana");
    if ans == "f":#if they had chosen fish they get asked white or teal?
        ans = input("white(w) or teal(t)?")
        if ans  == "w":#if white is chosen they are Elsa
            print("You are Elsa")
        else:#if teal is chosen they are jasmine
            print("You are Jasmine");
if ans =="f":#if they chose fall, they get asked bird or cat?
    ans = input("bird (b) or cat (c)?")
    if ans == "b":#if bird is chosen they get asked blue or red?
        ans = input("blue(b) or red(r)?")
        if ans  == "b":#if blue is chosen they are cinderella
            print("You are Cinderella")
        else:#if red is chosen they are snow white
            print("You are Snow White");
    if ans == "c":#if they chose cat, they get asked pink or yellow?
        ans = input("pink(p) or yellow(y)?")
        if ans  == "p":#if they chose pink they are sleeping beauty
            print("You are Sleeping Beauty")
        else:#if they chose yellow they are Belle
            print("You are Belle");
