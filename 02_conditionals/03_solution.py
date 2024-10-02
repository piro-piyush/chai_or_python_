# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

students_score = int((input("Enter Student's score : ")))

if students_score > 100 or students_score < 0:
    print("Please reverify your marks before entering")
    exit()

if students_score >= 90:
    Grade = "A"
elif students_score >= 80:
    Grade = "B"
elif students_score >= 70:
    Grade = "C"
elif students_score >= 60:
    Grade = "D"
else:
    Grade = "F"

print("Grade :", Grade)
