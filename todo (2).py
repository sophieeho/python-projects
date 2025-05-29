#Sophie
#Init
global groceryList
groceryList = []
#Function
print("welcome to your grocery list!")
def todolist():
    while True:
        try:
            todo = int(input("""#1. View the current to-do list
            #2. Add an item to the to-do list
            #3. Remove a task from the to-do list
            #4. Sort the list alphabetically
            #5. Count and print the # of items on the To-do List
            #6. Exit the program"""))
            if todo == 1:
                print(groceryList)
            elif todo == 2:
                added = input("what would you like to add to your grocery list?")
                groceryList.append(added)
            elif todo == 3:
                remove = input("what items would you like to remove from your grocery list?")
                groceryList.remove(remove)
            elif todo == 4:
                groceryList.sort()
            elif todo == 5:
                print(len(groceryList))
            elif todo == 6:
                print("thanks for using this list!")
                break
        except:
            print("ERROR: Must enter a number!")
#Main
todolist()

