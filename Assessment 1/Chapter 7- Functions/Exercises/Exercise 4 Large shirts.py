#show the shirts in different sizes
def make_shirt(size="large.", text='"Talk is cheap. Show me the code."'): #default size and message
    print("The size of the shirt will be " + size) #print the size of the shirt
    print(text + " would be a nice message.") #print the text on the shirt

make_shirt()
print("\n")
make_shirt(size="medium") 
print("\n")
make_shirt("extra small.", '"I love cats and dogs."') #the shirt on a different size and text
    