student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eve": 95,
    "Frank": 67,
}

student_grades = {}

for student in student_scores:
    if student_scores[student] >=91:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >=81:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >=71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)