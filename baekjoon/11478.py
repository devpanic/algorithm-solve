import sys

a = sys.stdin.readline().strip()
result = set()
max_len = len(a) - 1

for i in range(len(a)):
    for j in range(i, len(a)):
        result.add(a[i:j+1])
        
print(len(result))