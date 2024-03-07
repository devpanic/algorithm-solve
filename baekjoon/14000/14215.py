import sys

input_data = list(map(int, sys.stdin.readline().split()))
input_data.sort()

if input_data[2] >= input_data[0] + input_data[1]:
    print((input_data[1] + input_data[0]) * 2 - 1)
else:
    print(sum(input_data))