def calculate_result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >=80:
        grade = 'A'
    elif percentage >=60:
        grade = 'B'
    elif percentage >=50:
        grade = 'C'
    elif percentage >=40:
        grade = 'D'
    else:
        grade = 'F'

    print("Total:", total)
    print("Percentage:",percentage)
    print("Grade:",grade)

try:
    marks = list(map(int, input().split()))

    if len(marks) !=5:
        raise ValueError("Enter five marks")
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")

    calculate_result(marks)

except ValueError as e:
    print("Invalid input", e)