import sys

result = ["factor", "multiple", "neither"]

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        if a / b > 0 and a % b == 0:
            print(result[1])
        elif b / a > 0 and b % a == 0:
            print(result[0])
        else:
            print(result[2])
    except:
        break