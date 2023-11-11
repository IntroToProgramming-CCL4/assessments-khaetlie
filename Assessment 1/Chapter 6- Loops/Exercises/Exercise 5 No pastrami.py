sandwich_orders = ["Chicken sandwich", "pastrami", "Egg sandwich", "Grilled cheese", "pastrami", "Nutella sandwich", "pastrami"]

finished_sandwiches = [] #empty list

print("The deli ran out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami") #remove pastrami from the list

    order = sandwich_orders.pop()
    print("Your " + order + " will be ready soon.")
    finished_sandwiches.append(order) #move to the list of finished sandwiches

print("\n") #new line

for sandwich in finished_sandwiches:
    print("I finished making " + sandwich + " for you.") #the sandwiches were made