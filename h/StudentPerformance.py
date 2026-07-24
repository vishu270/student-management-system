import numpy as np

n = int(input("Enter the number of students: "))
students = []
subjects = np.array(['Math', 'Physics', 'Chemistry', 'python', 'Java'])

# input marks for each student
for i in range(n):
    name = input("Enter the name of student: ")
    students.append(name)
    marks = []
    for j in range(len(subjects)):
        mark = int(input("enter the marks of " + subjects[j] + ": "))
        marks.append(mark)
    print("marks of student:", marks)
    

#  output the results
i=0
for i in range(n):
    name = students[i]
    print("name of student:", name)
    print("Subjects and Marks:", subjects, marks)

    obtained_marks = sum(marks)
    print("obtained marks of student:", obtained_marks)
    percentage = (obtained_marks / 500) * 100
    print("percentage of student:", percentage)

if percentage >= 90:
    print("Grade: A")
if percentage >= 80:
        print("Grade: B")

# who get max percentage

max_percentage = 0
max_student = ""

for i in range(n):
    name = students[i]
    if percentage > max_percentage:
        max_percentage = percentage
        max_student = name

print("Student with topper:", max_student)
print("Maximum percentage:", max_percentage)