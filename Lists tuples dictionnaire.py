# 1. Choose 5 words from the English language and create  dictionaries that associates each of these words with its French translation.
words_translation = {}
words_translation['car']= 'voiture'
words_translation['house']='maison'
words_translation['computer']='ordinateur'
words_translation['table']='table'
words_translation['fridge']='frigo'

# 2. Add an entry to the dictionary of the previous question (a new word and its definition)
words_translation['screen']= ['ecran',"Surface sur laquelle se reproduit l'image d'un objet"]

# 3. How would you cut the following string at each space and put it in a list:
sentence = "I am the master of the world"
words = sentence.split()
print(words)

# 4. Transform this string "The_universal_number_is_42" by removing the underscores: "The universal number is 42"
universalNumber =  "The_universal_number_is_42"

universalNumber = universalNumber.replace("_"," ")
print(universalNumber)

#5. Display only values of this dictionary
heroes = {"Superman" : "Clark kent", "Batman" : "Bruce Wayne", "Spiderman" : "Tony Parker"}
print(heroes["Superman"],heroes["Batman"],heroes["Spiderman"])

# 6. Display only keys of this dictionary.
heroes = {"Superman" : "Clark kent", "Batman" : "Bruce Wayne", "Spiderman" : "Tony Parker"}
for x in heroes.keys():
    print (x)

# 7. Replace the value of "Spiderman" by "Peter Parker".
heroes = {"Superman" : "Clark kent", "Batman" : "Bruce Wayne", "Spiderman" : "Tony Parker"}

# 8. Create a dictionary to build the price base of the products corresponding to the following table:
""" Laser sword // 229.0
Mitendo DX // 127.30
Linux cushion // 74.50
Goldorak briefs // 29.90
Nextpresso station // 184.60 """

Price = {"Laser sword" : 229.0 , "Mitendo DX" : 127.30 ,
         "Linux cushion" : 74.50 ,"Goldorak briefs" : 29.90,
         "Nextpresso station" : 184.60}

# 9. Calculate the total price of the items of the dictionary
calculation = Price["Laser sword"] + Price["Mitendo DX"] + Price["Linux cushion"] +  Price["Goldorak briefs"] + Price["Nextpresso station"]
print(calculation)

# 10. Remove one of the articles from the dictionary
Price.pop('Laser sword')
print(Price)