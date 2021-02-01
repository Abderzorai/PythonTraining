#Create a variable age that contains value 42
age = 42
#Adds 10 to variable age
age += 10
#Create a variable ``divAge`` and assign it the value of the age divided by 7**   - ❗ Be careful, it must be an integer.
divAge = int(age/7)
#4. Create a variable textDiv that contains the character string "42 divided by 7 is equal 7". You must use the age and divAge variables'''
textDiv = "{} divided by 7 is equal {}".format(age,divAge)
#Create a variable restDiv that contains the rest of the variable age divided by 7
restDiv = int(age%7)
# Create a variable expDiv that contains the value of restDiv exponent 3
expDiv = int(restDiv**3)
#Write a program that enters an integer and then displays the value entered and its type.
integer = input("enter an integer")
print(integer,  type(integer))
#Use variables to represent the price of materials.
milk_price = 0.45
rawcider_price = 3.85
bag_of_flour_price= 0.9
Packet_of_butter_price = 0.77
Jar_of_nutella_price = 1.87
OrderPrice = int((milk_price*2)+(rawcider_price*3)+(bag_of_flour_price)+(Packet_of_butter_price)+(Jar_of_nutella_price))
print("The price is {} €".format(OrderPrice))
# Create a variable allowanceMoney which has a value of 20 and then create an algorithm that calculates the available money by subtracting the price of the order.
message = ""
# Declare and assign the variable ``allowanceMoney``
allowanceMoney = 20
# Then
if allowanceMoney > OrderPrice:
    print ("You have spent {} you have left {}".format(OrderPrice,allowanceMoney-OrderPrice))
elif allowanceMoney < OrderPrice:
    print ("Sorry you're missing {} euro".format(abs(allowanceMoney-OrderPrice)))
else:
    print ("You are broke!")

#Write a program that asks you to enter 2 values and displays the smallest of the 2 values
value1 = input("Enter a value")
value2 = input("Enter a second value")
if value1 < value2:
    print(value1)
elif value2 < value1:
    print(value2)

#Write a script that asks you to enter 2 strings and displays the largest of the 2 strings (the one with the most characters).
word1 = len(input("write a word"))
word2 = len(input("write another word"))

if word1 > word2:
   print(word1)
elif word2 > word1:
      print(word2)

#Write a script that converts euros into dollars.
currency = str(input("choose the currency you want to convert 'E' for euro and '$' for Dollars"))
Amount = int(input("What is the amount you want to convert"))

if currency == 'E':
    print("you have {} € which in dollars equal {} $".format(Amount,(Amount*1.21)))
elif currency == '$':
    print("you have {} $ which in dollars equal {} €".format(Amount,(Amount*0.81)))

# Check if the variable name is in the studentsTuring list. (Without making a loop)
studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]
name = "Julie"

if name in studentsTuring:
    print("You are at the turing's")
else:
    print("You are not part of the turing's")

#Calculate the volume of a sphere using the formula (4π/3) x R³. The radius is 10.

volume = (((4*3.14)/3)*(10**3))
print(volume)