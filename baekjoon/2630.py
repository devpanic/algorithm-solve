import sys

n = int(sys.stdin.readline().strip())
graph = []
result = [0, 0]  # white/blue
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))


def cut(x, y, width):
  init = graph[x][y]

  # 종료 조건
  if width == 1:
    result[init] += 1
    return

  break_flag = False

  # 공간을 구성하는 색이 1개인지 확인
  for i in range(x, x + width):
    for j in range(y, y + width):
      if i == x and j == y:
        continue
      if init != graph[i][j]:
        break_flag = True
        break
    if break_flag:
      break

  if not break_flag:
    result[init] += 1
    return

  # 작은 색종이로 나눔
  new_width = width // 2
  cut(x, y, new_width)
  cut(x, y + new_width, new_width)
  cut(x + new_width, y, new_width)
  cut(x + new_width, y + new_width, new_width)
  return


cut(0, 0, n)
print(result[0], "\n", result[1], sep="")
