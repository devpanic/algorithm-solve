# 1436.py
import sys

# n번쨰로 666 들어가는 숫자 찾기
input = int(sys.stdin.readline())

i = 666
j = 0
result = 0

while j != input:
  temp_str = str(i)
  if temp_str.count("666") != 0:
    result = i
    j += 1
  i += 1

print(result)
