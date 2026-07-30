print("Student Grade Analyzer")
print("-----------------------")

grades = []

while True:
    grade = input("Enter a grade (or type 'done' to finish): ")

    if grade.lower() == "done":
        break

    grades.append(float(grade))

if len(grades) == 0:
    print("No grades were entered.")
else:
    print("Grades:", grades)

    average = sum(grades) / len(grades)

    print("Average grade:", round(average, 2))

    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print("Average letter grade:", letter_grade)

    highest = max(grades)
    lowest = min(grades)

    print("Highest grade:", highest)
    print("Lowest grade:", lowest)