import sys

inputs = []
sum = 0

for _ in range(5):
    input = int(sys.stdin.readline())
    sum += input
    inputs.append(input)
inputs.sort()
print(int(sum / 5))
print(inputs[2])

