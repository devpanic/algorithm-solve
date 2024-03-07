import sys

n = int(sys.stdin.readline())

for k in range(n, 0, -1):
    for i in range(k - 1, 0, -1):
        print(" ", end = '')
    for j in range(0, n - k + 1):
        print("*", end = '')
    print("")