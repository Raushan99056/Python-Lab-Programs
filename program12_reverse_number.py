Write a python program to reverse a given number.

  # Program to reverse a given number

print("Reverse Number")
print("--------------")

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse of the given number is:", reverse)
