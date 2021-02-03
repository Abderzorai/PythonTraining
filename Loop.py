#  Display all students in the "students" list in alphabetical order
students =  ["Merouane", "Baptiste", "Caroline", "Joe", "Sophie", "Nathan", "Raphaël", "Axel", "Mathieu", "Adrien"]
print(sorted(students))

# Display only those whose first name begins with the letter M
for x in students:
    if (x[0] == 'M'):
        print(x)

# Display integers from 0 to 15 not included, using a "for"loop and the range() instruction.
for i in range(1,15):
    print(i)

#Use the "break" instruction
#to interrupt a "for" loop to display integers from 1 to 10 included, when the loop variable is 5
for x in range(0,11):
    print(x)
    if x == 5:
        break

#  Use the "continue" instruction to modify a "for" loop to display intergers from 1 to 10 included, when the loop variable is 5
modify???

# Follow the instructions :
listOfnum = [17, 38, 10, 25, 72]
print(sorted(listOfnum))
listOfnum.append(12)
print(sorted(listOfnum))
print(listOfnum)
Reversed_List = listOfnum[::-1]
print(Reversed_List)

# 7. Write an algorithm that asks the user to enter a number. Then make sure that your program displays all the numbers up to 0, for example, if the user enters the number 3, then your program will display something like this: 3,2,1,0
number_User = int(input("Enter a number"))
while number_User != -1:
    print(number_User)
    number_User -= 1

# 8.The price is right ! Create a variable that will contain the number to be found. Then create an algorithm that will ask the user to find this price. If the user enters a number that is too high, he will have the sentence: "It's less". If he enters a number that is too low, he will have the sentence: "It's more". If the user finds the right price he will have the sentence: "Well done, you won".


number_secret = int(5)
number_user = 0

while number_user != number_secret:
    number_user = int(input("write a number to find the secret number"))
    if number_user > number_secret:
        print("it's less than that")
        continue
    elif number_user < number_secret:
            print("it's more")
            continue
else:
    print('well done, you won')

# 9. Display all students with the sentence "NAME is a alumni. "
allStudents =  [["David", "Justine", "Valentin","Axel", "Redouane"], ["Julie", "Stéphane", "Mostapha", "Claudiu", "Son"]]
for x in allStudents:
    for x in x:
        print('{} is a alumni'.format(x))

# 10. Display all elements. If the element is part of the first table display - "PHP is a backend language" - and if the element is part of the second language, display - "HTML is a Frontend language" ...

languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]
for x in languages[0]:
    print('{} is a backend language'.format(x))
for x in languages[1]:
    print('{} is a Frontend language'.format(x))


