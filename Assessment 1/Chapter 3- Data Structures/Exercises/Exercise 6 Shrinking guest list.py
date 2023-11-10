names = ["Shrek", "Fiona", "Donkey", "Gingy"] #List of the original guests

print("You are invited to my dinner party this Saturday,", names [0]) #Print the message with the first guest on the list
print("You are invited to my dinner party this Saturday,", names [1]) #Print the message with the second guest on the list
print("You are invited to my dinner party this Saturday,", names [2]) #Print the message with the third guest on the list
print("You are invited to my dinner party this Saturday,", names [3]) #Print the message with the fourth guest on the list


#Update the current guest list to replace the guest who couldn't make it
names = ["Shrek", "Fiona", "Donkey", "Gingy"] #List of the original guest list
names[2] = "Rumpelstiltskin" #Name of the guest replaced by the previous guest
print(names) #Print the names of the updated guest list

#This is the second set of invitation messages for the poeple still on the list 
print("I would like to remind you about the dinner party this Saturday,", names [0]) #Print the message with the first guest on the list
print("I would like to remind you about the dinner party this Saturday,", names [1]) #Print the message with the second guest on the list
print("I would like to remind you about the dinner party this Saturday,", names [2]) #Print the message with the new guest on the list
print("I would like to remind you about the dinner party this Saturday,", names [3]) #Print the message with the fourth guest on the list

#inform guests that you only have limited space
print("We regret to inform everyone that we will be changing the guest list as there can only be a limit of two people allowed in the dinner party. We hope you understand and sorry for the incovenience.")

names.pop() #use pop() to remove guests from the list
print("Dear", names[2], "I regret to inform you that there will be a limited space in the party and we can only invite two people and have to cancel our invitation. We hope you understand.") #a message to everyone about the limited space

#inform remaining guests that they are still invited to the dinner party
print("Hi,", names[0], "I would like to inform you that you are still invited for the dinner party this Saturday. Thank you.") #inform the guest that they are no longer invited to the party
print("Hi,", names[1], "I would like to inform you that you are still invited for the dinner party this Saturday. Thank you") #inform the second guest that they are no longer invited to the party

#empty the list
del(names[0])
del(names[0])
del(names[0])

#print the empty list
print(names)