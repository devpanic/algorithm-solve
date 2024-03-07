import sys

m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

instructions = int(sys.stdin.readline())
expect = list(map(int, sys.stdin.readline().split()))


def bi_search(num):
  start = 0
  end = m - 1

  while start <= end:
    mid = (start + end) // 2
    if cards[mid] == num:
      return True
    elif cards[mid] > num:
      end = mid - 1
    else:
      start = mid + 1


for i in range(instructions):
  if bi_search(expect[i]):
    print("1", end=" ")
  else:
    print("0", end=" ")