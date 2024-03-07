import sys

data_num = int(sys.stdin.readline().rstrip())
dataset = list(map(int, sys.stdin.readline().split())) 
result = []

def getDivs(num):
    result = []
    for i in range(1, int(num ** (1/2)) + 1):
        if num % i == 0:
            result.append(i)
            if i**2 != num:
                result.append(num // i)
    return len(result)

for num in dataset:
    if getDivs(num) == 2:
        result.append(num)

print(len(result))