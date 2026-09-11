In certain university,grades are assigned to the marks obtained in respective subjects. Grades are assigned as given below. Write a python program to accept Marks in Math and display respective grade as an output usin if.....elif...elif..else statements(Using multiple conditions.)  
Hint: Relational operators: <,>,<=,>=,==,!=

Marks obtained                       Grade
90-100                                O
80-89                                 A+
70-79                                 A
60-69                                 B
50-59                                 C
40-49                                 P
Below 39                              F


  marks = int(input("Enter marks in Math: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
elif marks >= 40:
    print("Grade: E")
else:
    print("Grade: F")
