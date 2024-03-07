import sys

def getDiv(num):
    result = []
    for i in range(1, int(num ** (1/2) + 1)):
        if num % i == 0:
            result.append(i)
            if i * i != num:
                result.append(num % i)
    result.sort()
    return result

low = int(sys.stdin.readline().rstrip())
high = int(sys.stdin.readline().rstrip())
result = []

for i in range(low, high+1):
    cur_num = getDiv(i)
    if len(cur_num) == 2:
        result.append(i)

if len(result) == 0:
    print("-1")
else:
    print(sum(result))
    print(min(result))