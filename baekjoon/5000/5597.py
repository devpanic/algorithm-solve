import sys

students = [0 for _ in range(30)]

for _ in range(28):
    students[int(sys.stdin.readline()) - 1] = 1

for _ in range(2):
    print(students.index(0) + 1)
    students[students.index(0)] = 1