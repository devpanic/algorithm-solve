import sys

input = list(sys.stdin.readline().strip())

input.sort(reverse=True)

for chr in input:
    print(chr, end="")