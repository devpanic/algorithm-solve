import sys

total = [[] for _ in range(15)]

for _ in range(5):
    cur_dataset = list(map(str, sys.stdin.readline()[0:-1]))
    for i in range(len(cur_dataset)):
        total[i].append(cur_dataset[i])

for line in total:
    for chr in line:
        print(chr, end="")