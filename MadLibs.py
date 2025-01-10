#sophie
#MadLibs
personality = input("pick a positive personality trait")#list an personality trait
color = input("pick a color")#this gives to option to write any color
material1 = input("pick a material to build your house")#insert a material
material2 = input("pick a different material to build your house")#insert a different material
material3 = input("pick a different material to build your house")#insert a third material
size = input("pick a size description word")#insert a size description word
animal = input("pick an animal in plural")#this asks the player to pick an animal
animal2 = input("pick another animal in plural")#this asks to pick another animal
print("Once upon a time there were three little " + str(animal) + ". Each of them wearing " + str(color) + "shirts." +#this prints the story with all of the applicable words that the player chose
      "They built three " + str(size) + " houses. The first one built a house out of " + str(material1) + "." +
      " The second one built a house out of " + str(material2) + ". The last one built a house out of " + str(material3) + "." +
      " One day a big, bad " + str(animal2) + " tried to blow their houses down. Only the third house ended up surviving because the " +
      str(animal) + " was very " + str(personality) + " and chose " + str(material3) + "." )
