rivers = {'Amazon river': 'Peru', 'Yangtze': 'China', 'Ob': 'Russia'} #list of major rivers in the world
for river, country in rivers.items(): 
    print(river.title() + " runs through " + country.title()) #print the message about each river and where they belong
print("\n") #creates new line for the river names
for river in rivers.keys():
    print(river.title()) #print the name of each river
print("\n") #creates new line for the countries 
for country in rivers.values():
    print(country.title()) #print the name of each country