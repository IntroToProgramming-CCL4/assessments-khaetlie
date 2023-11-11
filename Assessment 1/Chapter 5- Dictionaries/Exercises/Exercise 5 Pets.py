pets = [] #this is an empty list

pet = {"animal kind": "Pomeranian", #information about the pet
       "pet name": "Oreo", 
       "owner": "May"
       }

pets.append(pet)

pet = {"animal kind": "Chihuahua", #information about the pet
       "pet name": "Peachy",
       "owner": "Leo"
       }

pets.append(pet)

pet = {"animal kind": "German Shepherd", #information about the pet
       "pet name": "Bruno",
       "owner": "Julie"
       }

pets.append(pet)

for pet in pets:
    print("\nAll about " + pet["pet name"].title())  
    for key, value in pet.items():
        print("\t" + key + ": " + str(value)) #print all the pet information
