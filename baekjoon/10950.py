import sys

num_tests = int(sys.stdin.readline())

for i in range(num_tests):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)