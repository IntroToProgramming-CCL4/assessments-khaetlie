while True:
 print("\n")
 print("----------Welcome to the School Supplies Vending Machine!----------")
 print("\n")
#user will enter the amount of money only less than or equal to 100
 amount_money = int(input("Please enter the amount of money (LIMIT of 100):")) 
 if amount_money <= 100: 
     print("\n")
     print("\t------------Please select your item-------------")
    #list of items
     item_one = {"code":"A1","name":"5-pcs highlighter","price":4.00}
     item_two = {"code":"A2","name":"12-pcs pencil","price":10.00}
     item_three = {"code":"A3","name":"12-pcs colored pencil","price":14.00}
     item_four = {"code":"A4","name":"5-pcs ballpoint pen","price":7.50}
     item_five = {"code":"A5","name":"4-pcs whiteboard marker","price":9.50}
     item_six = {"code":"B1","name":"100-pcs index card","price":8.50}
     item_seven = {"code":"B2","name":"10-pcs paintbrush set","price":6.00}
     item_eight = {"code":"B3","name":"glue stick","price":6.50}
     item_nine = {"code":"B4","name":"6-pcs eraser","price":3.00}
     item_ten = {"code":"B5","name":"400 sheets sticky notes","price":7.00}

    #place all items in a list
     all_items = [item_one,item_two,item_three,item_four,item_five,item_six,item_seven,item_eight,item_nine,item_ten] 

    #display the products
     print(f"CODE\tNAME\t\t\t\t\t\tPRICE\t") 
     for item in all_items:
        print(f"{item['code']:2}\t{item['name']:40}\t{item['price']:.2f}") 

    #ask the user to input the code of their chosen item
     print("\n")
     user_code = (input("Please enter the code of the item you'd like to purchase: "))
     your_item = None
     for item in all_items:
        if user_code == item['code']:
            your_item = item 
            print(f"You have selected: {your_item['name']}. Please pay: AED {your_item['price']:.2f}")
            break
        
         #check if there is any change to return
     def change (amount_money,cost): 
        if amount_money >= cost:
            change = amount_money - cost
            return change
        
     result = change (amount_money,your_item['price'])
     print(f"Payment Successful. Your change is AED {result:.2f}.")
     print("\t")
     
     
    #ask user if they want to continue shopping or quit
     print("\n")
     customer = input("Thank you for shopping! If you'd like to purchase again, type C. If you'd like to quit, type Q: ")
     if customer == "Q": #type Q if user wants to quit shopping and end the loop
        print("Thank you for shopping at the School Supplies Vending Machine!")
        break
      
#if the amount entered is more than AED 100 it will be invalid and return back to menu
 else:
    print("\t")
    print("Invalid. Please enter an amount of less than 100 only.")