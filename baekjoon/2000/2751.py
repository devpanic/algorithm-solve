import sys

n = int(sys.stdin.readline())
inputs = []

for _ in range(n):
    inputs.append(int(sys.stdin.readline()))

inputs.sort()

for input in inputs:
    print(input)