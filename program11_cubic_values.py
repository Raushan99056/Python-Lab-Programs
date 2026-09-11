write a python program to accept 5 numbers from the user and display their cubic values.


# Program to accept 5 numbers and display their cubic values

print("Cubic Value Calculator")
print("----------------------")

for i in range(1, 6):
    num = float(input("Enter number " + str(i) + ": "))
    cube = num ** 3
    print("Cubic value of", num, "is:", cube)
