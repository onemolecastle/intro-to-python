# Checkpoint exercise - after Loops - "Students" example.

# Student Data Structure
students = [
    {
        "id": 1,
        "name": "Alice",
        "grades": {"Math": 85, "Science": 92, "English": 88},
        "attendance": 95
    },
    {
        "id": 2,
        "name": "Bob",
        "grades": {"Math": 78, "Science": 80, "English": 76},
        "attendance": 90
    },
    {
        "id": 3,
        "name": "Charlie",
        "grades": {"Math": 90, "Science": 85, "English": 91},
        "attendance": 92
    }
]

# Exercise 1: Print names and IDs of all students
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}")

# Exercise 2: Calculate the average Math grade
total_math_grade = sum(student['grades']['Math'] for student in students)
average_math_grade = total_math_grade / len(students)
print(f"Average Math Grade: {average_math_grade}")

# Exercise 3: List students with attendance higher than 90%
high_attendance_students = [student['name'] for student in students if student['attendance'] > 90]
print(f"Students with high attendance: {high_attendance_students}")

# Exercise 4: Print the grades of each student
for student in students:
    print(f"{student['name']}'s Grades: {student['grades']}")

# Exercise 5: Find the student with the highest average grade
highest_avg_grade_student = max(students, key=lambda x: sum(x['grades'].values()) / len(x['grades']))
print(f"Student with the highest average grade: {highest_avg_grade_student['name']}")

# Exercise 6: Count the number of students who scored more than 85 in English
english_85_up = len([student for student in students if student['grades'].get('English', 0) > 85])
print(f"Students who scored more than 85 in English: {english_85_up}")

# Exercise 7: Update Science grades by 5% for all
for student in students:
    student['grades']['Science'] *= 1.05

# Exercise 8: Print the names of students whose average grade is more than 80
above_80_students = [student['name'] for student in students if sum(student['grades'].values()) / len(student['grades']) > 80]
print(f"Students with an average grade above 80: {above_80_students}")

# Exercise 9: List students who have taken all three subjects
all_subject_students = [student['name'] for student in students if len(student['grades']) == 3]
print(f"Students who have taken all three subjects: {all_subject_students}")

# Exercise 10: Calculate the overall average attendance
total_attendance = sum(student['attendance'] for student in students)
average_attendance = total_attendance / len(students)
print(f"Overall average attendance: {average_attendance}")
