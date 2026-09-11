Write a python program to determine whether a given year is a leap year or not.

# Program to check whether a given year is a leap year or not

print("Leap Year Checker")
print("-----------------")

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("The given year is a Leap Year.")
else:
    print("The given year is not a Leap Year.")
