import sys

input_string = sys.stdin.readline()[0:-1]
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

len_input_string = len(input_string)
result = 0

for char in croatia:
    if input_string.count(char) > 0:
        result += input_string.count(char)
        input_string = input_string.replace(char, '-')

input_string = input_string.replace("-", '')
result += len(input_string)
print(result)