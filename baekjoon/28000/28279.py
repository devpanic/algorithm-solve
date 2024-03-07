#28279 덱2
import sys
from collections import deque

instruction_count = int(sys.stdin.readline().rstrip())
data_set = deque()

for _ in range(instruction_count):
  current_instruction = list(sys.stdin.readline().split())
  data_count = len(data_set)
  match(current_instruction[0]):
    case '1':
      data_set.appendleft(current_instruction[1])
    case '2':
      data_set.append(current_instruction[1])
    case '3':
      if data_count == 0:
        print(-1)
      else:
        print(data_set.popleft())
    case '4':
      if data_count == 0:
        print(-1)
      else:
        print(data_set.pop())
    case '5':
      print(data_count)
    case '6':
      if data_count == 0:
        print(1)
      else:
        print(0)
    case '7':
      if data_count == 0:
        print(-1)
      else:
        print(data_set[0])
    case '8':
      if data_count == 0:
        print(-1)
      else:
        print(data_set[data_count-1])