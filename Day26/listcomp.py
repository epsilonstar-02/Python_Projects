import random

# names =["Fred","Alex","Beth","Alexander","Bethany","George"]
# short_names = [name.upper() for name in names if len(name)<5]
# print(short_names)
#
# integers = [1,2,3,4,5,6,7,8,9]
# even = [num for num in integers if num%2==0]
# print(even)
#
# with open("file1.txt","r") as num1:
#     file1 = num1.read().strip().splitlines()
#
# with open("file2.txt","r") as num2:
#     file2 = num2.read().strip().splitlines()
#
# common = [int(num) for num in file1 if num in file2]
# print(common)
#
# students = {student:random.randint(1,100) for student in names}
# print(students)
# passed = {student:marks for (student,marks) in students.items() if marks>50}
# print(passed)
#

# sentence = "What is your name boy?"
# words = sentence.split()
# count = {word:len(word) for word in words}
# print(count)

weather = {    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 13,
    "Friday": 16,
    "Saturday": 18,
    "Sunday": 20
}

weather_f = {day:(c*9/5)+32 for day,c in weather.items()}
print(weather_f)