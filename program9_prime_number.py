write a python program to check if given number is prime or not.


# Program to check whether a given number is prime or not

print("Prime Number Checker")
print("--------------------")

num = int(input("Enter a number: "))

if num <= 1:
    print("The given number is not a Prime Number.")

else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The given number is a Prime Number.")
    else:
        print("The given number is not a Prime Number.")
