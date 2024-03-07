import sys

input = int(sys.stdin.readline())

big = input // 5
small = input % 5

for i in range(0, big + 1):
    if (small + i * 5) % 3 == 0:
        small = (small + i * 5) // 3
        big = big - i
        break
    if i == big:
        small = -1

if small != -1:
    print(big + small)
else:
    print(small)