import sys

sys.setrecursionlimit(1000)

def is_same(head, tail, str, count):
  if head >= tail:
    return [1, count]
  elif str[head] == str[tail]:
    return is_same(head + 1, tail - 1, str, count + 1)
  else:
    return [0, count]

instructions = int(sys.stdin.readline())

for _ in range(instructions):
  input = sys.stdin.readline().strip()
  tail = len(input) - 1
  head = 0
  count = 1
  result = is_same(head, tail, input, count)
  print(result[0], result[1])
