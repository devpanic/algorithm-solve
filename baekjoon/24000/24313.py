import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().rstrip())
n0 = int(sys.stdin.readline().rstrip())

fn = a1 * n0 + a0
result = c * n0
# print(fn, result)
if fn <= result and (a1 <= c):
    print(1)
else:
    print(0)