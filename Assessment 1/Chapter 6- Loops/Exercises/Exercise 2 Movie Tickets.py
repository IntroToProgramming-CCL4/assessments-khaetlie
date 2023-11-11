age = int(input("Enter your age:"))

if age <= 3: 
    print("The ticket is free.") #This is the price of the ticket for people under the age of 3
elif age <= 12:
    print("The ticket price is $10.") #This is the price for people between the age of 3 to 12
elif age > 12:
    print("THe ticket price is $15.") #This is the price for people over the age of 12
