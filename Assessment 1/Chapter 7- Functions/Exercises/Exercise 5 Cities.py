#describe a city
def describe_city(city, country="Poland"):
    sentence = "The capital of " + country.title() + " is" + city.title() + "."
    print(sentence)

#call funciton for different cities 
describe_city(" Bamako") 
describe_city(" Tallinn","Estonia")
describe_city(" Warsaw")
