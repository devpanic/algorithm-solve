import sys

grades = [["A+", 4.5], ["A0", 4]
          , ["B+", 3.5], ["B0", 3]
          , ["C+", 2.5], ["C0", 2]
          , ["D+", 1.5], ["D0", 1]
          , ["F", 0]]
total_grade = 0.0
total_grade_num = 0.0

for i in range(20):
    sub, time, grade = map(str, sys.stdin.readline().split())
    if grade != "P":
        for find_grade in grades:
            if grade == find_grade[0]:
                total_grade += find_grade[1] * float(time)
                total_grade_num += float(time)

print(round(total_grade / total_grade_num, 6))