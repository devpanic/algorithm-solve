import sys

input_str = sys.stdin.readline()[0:-1]
len_str = len(input_str)
isPalin = 1

for i in range(len_str):
    if input_str[i] != input_str[len_str - i - 1]:
        isPalin = 0

print(isPalin)