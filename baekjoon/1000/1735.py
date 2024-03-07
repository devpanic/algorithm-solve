# 기약분수의 합을 구하는 문제였다
# 우선 두 분수의 합을 구한 뒤 해당 분수의 기약분수를 구했다
import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

new_a = (a*d + c*b)
new_b = b*d

origin_a = new_a
origin_b = new_b

while new_b > 0:
    new_a, new_b = new_b, new_a % new_b

lcm = int((origin_a * origin_b) / new_a)

print(int(origin_a / new_a), int(origin_b / new_a))