import sys

def reverse_str(to_reverse):
    temp_string =""
    for i in range(len(to_reverse) - 1, -1, -1):
        temp_string += to_reverse[i]
    return temp_string

a, b = map(str, sys.stdin.readline().split())

reversed_a = reverse_str(a)
reversed_b = reverse_str(b)

if int(reversed_a) > int(reversed_b):
    print(reversed_a)
else:
    print(reversed_b)