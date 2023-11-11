programming_words = { #dictionary of five programming words with their meanings
    "Variable": "a reserved memory location to store values.",
    "Operator": "are symbols or keywords that designate some type of computation.",
    "Dictionary": "a collection of key-value pairs.",
    "list": "a data structure that is mutable, changeable, ordered sequence of elements.",
    "Functions": "a block of statements that return the specific task.",
    "string": "A series of characters.",
    }

#Print the word 'variable' with its meaning
meaning = "Variable" 
print("\n" + meaning.title() + ": " + programming_words[meaning]) #

#Print the word 'Operator' with its meaning
meaning = "Operator"
print("\n" + meaning.title() + ": " + programming_words[meaning])

#Print the word 'Dictionary' with its meaning
meaning = "Dictionary"
print("\n" + meaning.title() + ": " + programming_words[meaning])

#Print the word 'list' with its meaning
meaning = "list"
print("\n" + meaning.title() + ": " + programming_words[meaning])

#Print the word 'Functions' with its meaning
meaning = "Functions"
print("\n" + meaning.title() + ": " + programming_words[meaning]) 

for meaning, define in programming_words.items():
    print("\n" + meaning.title() + ": " + define)