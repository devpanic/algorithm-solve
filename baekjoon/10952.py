import sys
a = 1
b = 1
while (a + b) != 0:
    a,b = map(int, sys.stdin.readline().split())
    if (a + b) !=  0:
        print(a + b)