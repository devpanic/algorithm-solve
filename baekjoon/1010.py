import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    n, m = map(int, sys.stdin.readline().split())

    upper = 1
    lower = 1

    for i in range(n + 1, m + 1):
        upper = upper * i
    for i in range(1, m - n + 1):
        lower = lower * i
    
    print(upper // lower)