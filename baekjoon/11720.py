import sys
num = map(int, sys.stdin.readline().split())
num_list = list(sys.stdin.readline()[0:-1])
sum = 0

for i in num_list:
    sum += int(i)

print(sum)