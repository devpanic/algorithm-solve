import sys

sys.setrecursionlimit(10**9)
count = -1
order = [[1, 3], [2, 4]]
done = False
n, answer_x, answer_y = map(int, sys.stdin.readline().split())


def go_z(num, x, y):
  global count
  if answer_x < x or answer_x >= x + num or answer_y < y or answer_y >= y + num:
    count += num * num
    return

  if num == 2:
    count += order[answer_y - y][answer_x - x]
    print(count)
    return

  # 재귀 호출
  new_num = num // 2
  go_z(new_num, x, y)
  go_z(new_num, x, y + new_num)
  go_z(new_num, x + new_num, y)
  go_z(new_num, x + new_num, y + new_num)


go_z(2**n, 0, 0)
