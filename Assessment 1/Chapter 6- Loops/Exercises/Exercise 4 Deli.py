sandwich_orders = ["Chicken sandwich", "Egg sandwich", "Grilled cheese", "Nutella sandwich"] #list of sandwiches
finished_sandwiches = [] #empty list

while sandwich_orders:
    order = sandwich_orders.pop()
    print("Your " + order + " will be ready soon.")
    finished_sandwiches.append(order) #move to the list of finished sandwiches

print("\n") #new line

for sandwich in finished_sandwiches:
    print("I finished making " + sandwich + " for you.") #the sandwiches were made