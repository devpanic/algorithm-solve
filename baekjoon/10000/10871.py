import sys

n, x = map(int, sys.stdin.readline().split())
lists_n = list(map(int, sys.stdin.readline().split()))

for element in lists_n:
    if element < x:
        print(element,"", end='')
print("")