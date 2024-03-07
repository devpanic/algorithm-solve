# 1710번 - 골트바흐의 추측
# 현재 케이스보다 작은 소수 리스트 구함
# 현재 숫자 - 소수 = 소수리스트에 있는지 판단
import sys

cases = int(sys.stdin.readline())
inputs = []
for _ in range(cases):
  inputs.append(int(sys.stdin.readline()))

max_val = max(inputs)
nums = [True for _ in range(max_val + 1)]
nums[0], nums[1] = False, False

# 입력된 수 중 가장 큰 수를 기준으로 소수 구하기
for i in range(2, int(max_val**(1 / 2)) + 1):
  if nums[i]:
    j = 2
    while i * j <= max_val:
      nums[i * j] = False
      j += 1

for input in inputs:
  count = 0
  for j in range(2, int(input / 2) + 1):
    if nums[j] and nums[input - j]:
      count += 1
  print(count)
