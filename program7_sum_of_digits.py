write a python program to print sum of all the digits of given number.


  # Program to find the sum of all digits of a given number

print("Sum of Digits")
print("-------------")

num = int(input("Enter a number: "))

# Convert negative number to positive
num = abs(num)

sum_of_digits = 0

while num > 0:
    digit = num % 10
    sum_of_digits = sum_of_digits + digit
    num = num // 10

print("Sum of all digits:", sum_of_digits)
