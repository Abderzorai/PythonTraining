# 1. Say Hello
# Write a function called hello(name) that returns a string of characters. This function will take as argument a variable name. This function will return a string 'Hello name'
def hello(name = "Anonymous"):
    return "Hello {}".format(name)
hello()

#2. Count students
#Create a function "sumOfStudents()" that calculates and returns the number of students in a list. The function will have to return an integer.
students = ([["Jean", "Alice", "Edwige", "Peter", "James"],
             ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]])


def sumOfStudents(students):
    y = 0
    for x in (students[0] + students[1]):
        y += 1
    return y


sumOfStudents(students)

#3. Is divisible ?
#Create a function isDivisible(n, x, y) that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.
def is_divisible(n,x,y):
    if n%x==0 and n%y==0:
        print(n==n,'because {} is divisible by {} and {}'.format(n,x,y))
    elif n%x==0 or n%y==0:
        if n%x!=0:
            print(n!=n,"because {} is not divisible by {}".format(n,x) )
        elif n%y!=0:
            print(n!=n,"because {} is not divisible by {}".format(n,y) )
    else:
        print(n!=n,"because {} is not divisible by {} nor {}".format(n,x,y))

is_divisible(10,5,8)

# 4. Abbreviate a Two Words Name
#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
name = input('what is your name and last name?')
def abbrevName(name):
    first_letter = name[0]
    name = name.split()
    a = name[0]
    b = name[1]
    return "{}.{}".format(a[0].upper(),b[0].upper())
abbrevName(name)

# 5Sum of positive
# You get an array of numbers, return the sum of all of the positives ones.
numbers = [1,-4,7,12]
def positive_sum(numbers):
    y =0
    for x in numbers:
        if x>0:
            y+=x
    return y
positive_sum(numbers)

#6. Sum mixed array
#Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#Return your answer as a number.
arr = ['5', '0', 9, 3, 2, 1, '9', 6, 7]
def sum_mix(arr):
    y=0
    for x in arr:
        x = int(x)
        y += x
    return y
sum_mix(arr)

"""7. Return the day
Complete the function which returns the weekday according to the input number:

1 returns "Sunday"
2 returns "Monday"
3 returns "Tuesday"
4 returns "Wednesday"
5 returns "Thursday"
6 returns "Friday"
7 returns "Saturday"
Otherwise returns "Wrong, please enter a number between 1 and 7"
"""
num = int(input('give me the number of the day'))
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
def whatday(num):
    num -= 1
    return "{}".format(days[num])
whatday(num)

#8. Summation
#Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
def summation(num):
    number=0
    while num != 0:
        number += num
        num -= 1
    return number
summation(8)

#9. If you can't sleep, just count sheep!!
#Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

sheep = " sheep..."


def count_sheep(n):
    x = 1
    while x <= n:
        print("{} {}".format(x, sheep))
        x += 1


count_sheep(4)

"""10. Student's final grade¶
Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.

This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);

This function should return a number (final grade). There are four types of final grades:

100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
0, in other cases"""

def final_grade(exam, projects):
    if exam > 90 or projects> 10:
        return 100
    elif exam>75 and projects>=5:
        return 90
    elif exam>50 and projects>=2:
        return 75
    else:
        return 0

final_grade(100,12)
final_grade(75,5)



# test code :
import unittest


class TestNotebook(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), 'Hello Anonymous')
        self.assertEqual(hello("Jean"), 'Hello Jean')

    def test_sumOfStudents(self):
        self.assertEqual(sumOfStudents(
            [["Jean", "Alice", "Edwige", "Peter", "James"], ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]]),
                         10)

    def test_is_divisible(self):
        self.assertEqual(is_divisible(3, 3, 4), False)
        self.assertEqual(is_divisible(12, 3, 4), True)
        self.assertEqual(is_divisible(8, 3, 4), False)
        self.assertEqual(is_divisible(48, 3, 4), True)

    def test_abbrevName(self):
        self.assertEqual(abbrevName("Sam Harris"), "S.H");
        self.assertEqual(abbrevName("Patrick Feenan"), "P.F");
        self.assertEqual(abbrevName("Evan Cole"), "E.C");
        self.assertEqual(abbrevName("P Favuzzi"), "P.F");
        self.assertEqual(abbrevName("David Mendieta"), "D.M");

    def test_positive_sum(self):
        self.assertEqual(positive_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(positive_sum([1, -2, 3, 4, 5]), 13)
        self.assertEqual(positive_sum([-1, 2, 3, 4, -5]), 9)
        self.assertEqual(positive_sum([]), 0)
        self.assertEqual(positive_sum([-1, -2, -3, -4, -5]), 0)

    def test_sum_mixed_array(self):
        self.assertEqual(sum_mix([9, 3, '7', '3']), 22)
        self.assertEqual(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)
        self.assertEqual(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']), 41)
        self.assertEqual(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']), 45)
        self.assertEqual(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)

    def test_return_day(self):
        self.assertEqual(whatday(1), 'Sunday')
        self.assertEqual(whatday(2), 'Monday')
        self.assertEqual(whatday(3), 'Tuesday')
        self.assertEqual(whatday(8), 'Wrong, please enter a number between 1 and 7')
        self.assertEqual(whatday(20), 'Wrong, please enter a number between 1 and 7')

    def test_final_grade(self):
        self.assertEqual(final_grade(100, 12), 100)
        self.assertEqual(final_grade(85, 5), 90)

    def test_count_sheep(self):
        self.assertEqual(count_sheep(1), "1 sheep...");
        self.assertEqual(count_sheep(2), "1 sheep...2 sheep...")
        self.assertEqual(count_sheep(3), "1 sheep...2 sheep...3 sheep...")

    def test_summation(self):
        self.assertEqual(summation(1), 1)
        self.assertEqual(summation(8), 36)


unittest.main(argv=[''], verbosity=2, exit=False)