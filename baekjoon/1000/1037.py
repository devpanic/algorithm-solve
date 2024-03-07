#1037.py
import sys

# sort 해서 홀/짝 판별 후 곱셈 ㄱㄱ
counts = int(sys.stdin.readline())
divs = list(map(int, sys.stdin.readline().split()))
divs.sort()

if counts == 1:
  print(divs[0]**2)
elif counts % 2 == 0:
  print(divs[0] * divs[counts - 1])
else:
  print(divs[int(counts / 2)]**2)
