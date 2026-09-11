write a python code to check given number is positive,negative or zero.


# Program to check whether a number is positive, negative, or zero

print("Number Checker")
print("--------------")

num = float(input("Enter a number: "))

if num > 0:
    print("The given number is Positive.")

elif num < 0:
    print("The given number is Negative.")

else:
    print("The given number is Zero.")
