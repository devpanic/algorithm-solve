import sys

while True:
  n = int(sys.stdin.readline()) + 1
  count = 0

  if n == 1:
    break
  elif n == 2:
    print(1)
    continue

  m = 2 * (n - 1)
  nums = [True for _ in range(m + 1)]
  nums[0], nums[1] = False, False

  for i in range(2, int(m**(1 / 2)) + 1):
    if nums[i]:
      j = 2
      while i * j < m:
        nums[i * j] = False
        j += 1

  for i in range(n, m):
    if nums[i]:
      count += 1
  print(count)
