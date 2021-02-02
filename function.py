#Create a variable countAlpha that contains the number of characters contained in the string "Hello world!"..
countAlpha = len("Hello world!")
print(countAlpha)
#Create a variable countFloat and cast the variable countAlpha in float
countFloat = float(countAlpha)
print(countFloat)
#Round the variable pi value to -10² and save it in a variable roundPi.
import math
pi = math.pi
roundPi = round(pi,2)
print(roundPi)
#Create a variable reversedText which contains the character string "Hello world !" upside down.
#The result must be a list() value.
slicedString =list('Hello world !')
stringlength=len(slicedString)
reversedText=slicedString[stringlength::-1]
# Create a variable age and ask the user to enter his age. Then display it and display its type.
age = input("what is your age?")
print(age,type(age))
#Create a variable sortNum that contains the sorted num list.
num = [2, 8, 1, 4, 6, 3, 7]
sortNum= sorted(num)
print(sortNum)
# Create a variable sumOfList which contains the sum of all the elements in the list num¶
num = [2, 8, 1, 4, 6, 3, 7]
sumOfList = sum(num)
print(sumOfList)
#Create a variable minValue that contains a minimum value of list num
num = [2, 8, 1, 4, 6, 3, 7]
minValue = min(num)
print(minValue)
#Create a variable maxValue that contains a maximum value of list num
maxValue= max(num)
print(maxValue)
# Find a function that will interpret the string of the variable calc
#Save the result in a variable named stringInterpret
calc  = "1 + 2"
stringInterpret = eval(calc)
print(stringInterpret)


#Testing
import unittest


class TestNotebook(unittest.TestCase):

    def test_countAlpha(self):
        self.assertEqual(countAlpha, 12)

    def test_countFloat(self):
        self.assertEqual(type(countFloat), type(float()))

    def test_pi(self):
        self.assertEqual(3.14, roundPi)

    def test_reversed(self):
        self.assertEqual(reversedText, ['!', ' ', 'd', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'H'])

    def test_age(self):
        self.assertEqual(type(age), type(str()))

    def test_sorted(self):
        self.assertEqual(sortNum, [1, 2, 3, 4, 6, 7, 8])

    def test_sum(self):
        self.assertEqual(sumOfList, 31)

    def test_min(self):
        self.assertEqual(minValue, 1)

    def test_max(self):
        self.assertEqual(maxValue, 8)


unittest.main(argv=[''], verbosity=2, exit=False)