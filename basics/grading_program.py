# Grading Program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermonie": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

# Iterate every key (names in our situation), evaluate their values and print according to that value some prints.
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding!"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
