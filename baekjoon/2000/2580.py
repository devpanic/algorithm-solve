# dfs까지는 생각했지만 백트래킹 조건을 찾아내지 못함 -> 기초 백트래킹 좀 더 풀어봐야 할것 같다
import sys

sdoku = []
zero_count = 0
zero_position = []
row = 0

for _ in range(9):
  temp = list(map(int, sys.stdin.readline().split()))
  for i in range(9):
    if temp[i] == 0:
      zero_count += 1
      zero_position.append([row, i])
  sdoku.append(temp)
  row += 1


def check(x, y, i):
  # 1. 열 확인
  for j in range(9):
    if sdoku[x][j] == i:
      return False

  # 2. 행 확인
  for j in range(9):
    if sdoku[j][y] == i:
      return False

  # 3. 칸 확인 with 이차원 배열 슬라이싱
  cell_x = x // 3
  cell_y = y // 3
  cell = [
      row[cell_y * 3:(cell_y + 1) * 3]
      for row in sdoku[cell_x * 3:(cell_x + 1) * 3]
  ]

  for j in range(3):
    for k in range(3):
      if cell[j][k] == i:
        return False
  return True


def dfs(k):
  if k == zero_count:
    for row in sdoku:
      print(' '.join(map(str, row)))
    exit()

  x = zero_position[k][0]
  y = zero_position[k][1]
  for i in range(1, 10):
    if check(x, y, i):
      sdoku[x][y] = i
      dfs(k + 1)
      sdoku[x][y] = 0


dfs(0)
