# Programmer:Deborah Onyuka
# Course:  CS201.01T, Dr. Olsen
# Date:[10/04/2016)
# Programming Assignment:PA2
# Problem Statement:Design a game that will have different paths based on the users input.
# Data In:A series of inputs that will then make descisions and give specific outputs
# thus creating different versions of the story
# Data Out:Specific outputs from the decisions made based on the input
# Credits:Class Notes 7-10 covering  if statements and nested if structures & the  Python Programming Textbook
#(boolean operators and chained operators)

print("Welcome to Deborah's Adventure Game!")

name = str(input("Please enter your name:"))

print("Hello", name, "we are going to go on an adventure in the Amazon Rain Forest!")

answer = str(input("Would you like to go on an adventure in the forest to find rare precious jewels? (yes or no )?"))
if answer =="no":
    print("I'm sorry to hear that.Come back and play next time.")
elif answer == "yes":
    path=int(input("There are three paths leading to the cave with the jewels which one will you take?(1,2 or 3)"))
    if path == 1:
        print(name, "You have chosen the first path,unfortunately this path has quicksand and you get trapped.Sorry")
    elif path == 2:
        print("This path is walkable however there are many wild animals and insects.A venomous spider jumps out "+
"and bites you and you are paralyzed.Better luck next time!")
    elif path == 3:
        print(name,"You have made an excellent choice you have chosen the right path it is clear and safe.")
        tribes=int(input("How many amazonian tribes do you want to help you?"))
        if tribes >= 20:
            print("You can't have that much help!")
        elif tribes <=3:
            print("You're going to need more help than that.You don't know the forest that well.They are supposed to guide you.")
        elif tribes < 20 and tribes > 3:
            print("You and the tribes stop on your way to the cave to eat some bananas that are hanging from the tree")
            bananas_eaten = float(input("How many bananas did you eat?(you can enter this answer in decimal form)"))
            if bananas_eaten >= 30:
                print("One of the bananas you have eaten was contaminated with a rare poison.")
            elif bananas_eaten <= 10:
                print("You've barely eaten, you faint because you haven't eaten enough and have to go to the hospital.Oh no!")
            else:
                print("The number of bananas eaten is", bananas_eaten)
                color=str(input("You and the tribe find the cave with precious jewels each on top of separate rocks."+
                  "there are three precious jewels one purple, one red and one blue.Which one do you choose?"))
                if color =="red":
                    print("You chose the red jewel!Unfortunately that jewel was booby trapped and you are now trapped"+
                 " under a net and the jewel disappears into the ground.")
                elif color == "purple":
                    print("You chose the purple jewel.You successfully take the jewel.You become rich and famous for" +
                  "finding this jewel.Congratulations!")

                elif color == "blue":
                    print("You chose the blue jewel!The tribes ambush you and try to steal the jewel and you realize you have been set up."+
         "However you successfully fight them off but you end up losing the jewel in the process.")

print("Bye!!!Thanks for trying out this game!")




