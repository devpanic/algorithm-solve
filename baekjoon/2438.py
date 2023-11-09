import sys

n = int(sys.stdin.readline())

for j in range(n):
    for i in range(0, j + 1):
        print("*", end='')
    print("")