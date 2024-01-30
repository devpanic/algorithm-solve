# 2231.py
# ref : https://develop247.tistory.com/344
import sys

input = int(sys.stdin.readline().strip())
result = 0

for i in range(1, input + 1):
    result = i + sum(map(int, str(i)))
    if result == input:
        print(i)
        break
    if i == input:
       print(0)
       break
