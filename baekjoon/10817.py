import sys

input = list(map(int, sys.stdin.readline().split()))
input.sort()

print(input[1])