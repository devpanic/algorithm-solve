import sys

n = int(sys.stdin.readline())

counts = [0 for _ in range(10001)]

for _ in range(n):
    input = int(sys.stdin.readline())
    counts[input] += 1

for i in range(len(counts)):
    while counts[i] > 0:
        print(i)
        counts[i] -= 1