human = input("Are you human?: ")
if human.capitalize() == 'Yes':
    print(" ")
    print("You're human, Good. You may continue.")
    name = input("Input Your Human Name : ")
    print("      ")
    print("Hello," + " " + name.capitalize())
    print("      ")

    age = int(input(name.capitalize() + " " + "Please enter your human age? "))
    if age > 30:
            # x > 0, y > 0
            print(" That appears to be old.")
    else:
            # x > 0, y <= 0
            print("That is pretty young for a human")
    # if letters -> invalid
    How = input("How are you today?")
    print("    ")

    print(How.capitalize())
    print("      ")
    print("Hmmm... ") 
    print("           ")

    print("That is a very human response" + "   ")
    print("      ")
else:
    not_human = input("What are you? ")
    print("That is very unusual")
    name = input("Input Your Name Being: ")
    print("      ")
    print("Hello," + " " + name)
    print("      ")

    age = int(input(name + " " + "Please enter the time you have been alive? "))
    print("    ")
    if age > 30:
            # x > 0, y > 0
            print(" That appears to be old.")
    else:
            # x > 0, y <= 0
            print("That is pretty young for a being like you.")
    # if letters -> invalid
    print("    ")
    How = input("How are you today?")
    print("    ")

    print(How)
    print("      ")
    print("Hmmm... ") 
    print("           ")

    print("That is a very human response" + "   ")
    print("      ")

