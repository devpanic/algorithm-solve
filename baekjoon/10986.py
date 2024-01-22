# 10986번 나머지 합
# https://www.acmicpc.net/problem/10986
# ref : https://only-wanna.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-10986%EB%B2%88-%EB%82%98%EB%A8%B8%EC%A7%80-%ED%95%A9
# https://velog.io/@dev-junku/BOJ-%EB%82%98%EB%A8%B8%EC%A7%80-%ED%95%A9-in-Python
# 나머지를 따로 관리하며 조합으로 푸는 문제
import sys

n, m = map(int, sys.stdin.readline().split())
sums = list(map(int, sys.stdin.readline().split()))
divs = [0 for _ in range(m)]
divs[0] = 1

count = 0
current_sum = 0

for i in range(n):
  current_sum += sums[i]
  divs[current_sum % m] += 1

# 조합 : n(n-1) / 2
# 나머지가 같은 부분합 중 무작위 추출해서 연산하면 모두 정답에 해당됨
for i in range(m):
  count += divs[i] * (divs[i] - 1) // 2
print(count)

# 완전 탐색으로 합의 나머지 연산
# n^2 -> 시간 초과
# for i in range(1, n + 1):
#   for j in range(i + 2, n + 1):
#     if sums[j] - sums[i] == 0:
#       count += 1
