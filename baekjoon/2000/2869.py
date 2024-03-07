import sys

up, down, goal = map(int, sys.stdin.readline().split())

gap = up - down
result = (goal - up) // gap
result_rest = (goal - up) % gap
# print("result : ", result)

if goal == up:
    print(1)
elif result_rest > 0:
    print(result + 2)
else:
    print(result + 1)