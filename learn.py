student_grades ={}
n=int(input())
for i in range(n):
    name,grade = input().split()
    student_grades[name]=int(grade)
print(student_grades)