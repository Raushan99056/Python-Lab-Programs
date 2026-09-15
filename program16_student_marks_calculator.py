Accept Student Name,Roll Number and Marks of the 3 subjects from the user. Calculate the percentage of the marks and display it. Display the subject with Highest and lowest marks.



# Accept student details
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

# Accept marks
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

# Calculate percentage
total_marks = marks1 + marks2 + marks3
percentage = total_marks / 3

# Find highest and lowest marks
marks = {
    "Subject 1": marks1,
    "Subject 2": marks2,
    "Subject 3": marks3
}

highest_subject = max(marks, key=marks.get)
lowest_subject = min(marks, key=marks.get)

# Display results
print("\n--- Student Result ---")
print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Percentage:", percentage, "%")
print("Highest Marks:", highest_subject, "-", marks[highest_subject])
print("Lowest Marks:", lowest_subject, "-", marks[lowest_subject])
