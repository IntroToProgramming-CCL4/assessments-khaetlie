alien_color = "green" #color of the alien

if alien_color == "red": #run the if block if the color of the alien is red
    print("You earned 15 points!") #the points earned by the user if the alien is red
elif alien_color == "yellow": #run the elif block if the color is yellow
    print("You earned 10 points!") #the points earned by the user if the color is yellow
else: #run the else block if the alien is green
    print("You earned 5 points!")

alien_color = "yellow"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "red":
    print("You earned 15 points!")
else:
    print("You earned 10 points!")

alien_color = "red"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You are earned 15 points!")