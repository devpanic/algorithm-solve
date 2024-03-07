import sys

alphabets = []

for i in range(97, 123):
    alphabets.append(chr(i))

input_data = list(sys.stdin.readline()[0:-1])

for i in alphabets:
    if i in input_data:
        print(input_data.index(i), end="")
    else:
        print("-1", end="")
    print(" ", end="")