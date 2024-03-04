import sys

num = int(sys.stdin.readline().strip())
result = [0, 0, 0]
graph = []

for _ in range(num):
  graph.append(list(map(int, sys.stdin.readline().split())))


def cut(x, y, width, is_cutted_nine):
  init_val = graph[y][x]
  same_flag = True
  temp = [0, 0, 0]

  if is_cutted_nine:
    for i in range(y, y + 3):
      for j in range(x, x + 3):
        val = graph[i][j]
        if init_val != val:
          same_flag = False
        temp[val] += 1
    if not same_flag:
      result[0] += temp[0]
      result[1] += temp[1]
      result[2] += temp[2]
      return
    else:
      result[init_val] += 1
  else:
    for i in range(y, y + width):
      for j in range(x, x + width):
        if init_val != graph[i][j]:
          same_flag = False
          break
      if not same_flag:
        break
    if same_flag:
      result[init_val] += 1
      return
    else:
      for i in range(y, y + width, 3):
        for j in range(x, x + width, 3):
          cut(j, i, 3, True)


if num == 3:
  cut(0, 0, num, True)
else:
  cut(0, 0, num, False)
print(result[-1])
print(result[0])
print(result[1])
