import sys

count = int(sys.stdin.readline())
input = []

for _ in range(count):
    x, y = map(int, sys.stdin.readline().split())
    input.append([x, y])

input.sort(key=lambda x:(x[1], x[0]))

for data in input:
    print(data[0], data[1])