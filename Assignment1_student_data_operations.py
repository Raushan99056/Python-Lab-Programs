Write a python program to create a Dictionary,Tuple and List of students and perform the following operations on the dictionary: Add,Delete,Update.
```python
# Create a List of students
students_list = ["Rahul", "Priya", "Amit", "Sneha"]

# Create a Tuple of students
students_tuple = ("Rahul", "Priya", "Amit", "Sneha")

# Create a Dictionary of students
students_dict = {
    101: "Rahul",
    102: "Priya",
    103: "Amit",
    104: "Sneha"
}

print("Student List:")
print(students_list)

print("\nStudent Tuple:")
print(students_tuple)

print("\nStudent Dictionary:")
print(students_dict)

# Add a student to the dictionary
students_dict[105] = "Neha"
print("\nAfter Adding a Student:")
print(students_dict)

# Update a student's name
students_dict[103] = "Ankit"
print("\nAfter Updating Student:")
print(students_dict)

# Delete a student
del students_dict[102]
print("\nAfter Deleting a Student:")
print(students_dict)
```
