countries = ["South Korea", "France", "Italy", "Fiji", "Poland"]
print(countries) #original order

#alphabetical order
print(sorted(countries))

#original order
print(countries)

#reverse order
countries.reverse()
print(countries)

#reverse order to return to the original order
countries.reverse()
print(countries)

#sort to return to the alphabetical order
countries.sort()
print(countries)

#sort to return to the reverse alphabetical order
countries.sort(reverse=True)
print(countries)