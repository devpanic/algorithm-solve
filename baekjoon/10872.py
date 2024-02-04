import sys

input = int(sys.stdin.readline())

result = 1

while input > 0 :
    result = result * input
    input -= 1

print(result)