import sys

a, b = map(int, sys.stdin.readline().split())
result = []

for i in range(1, int(a ** (1/2)) + 1):
    if a % i == 0:
        result.append(i)
        if i**2 != a:
            result.append(a // i)
result.sort()
if b > len(result):
    print(0)
else:
    print(result[b - 1])
