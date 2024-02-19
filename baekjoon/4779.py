import sys

sys.setrecursionlimit(10**6)
string = []


def canto(start, end):
  temp = end - start
  temp_div = temp // 3
  if temp != 1:
    pivots = [[start, start + temp_div],
              [start + temp_div, start + 2 * temp_div],
              [start + 2 * temp_div, end]]
    for i in range(pivots[1][0], pivots[1][1]):
      string[i] = " "
    canto(pivots[0][0], pivots[0][1])
    canto(pivots[2][0], pivots[2][1])
  else:
    return


while True:
  try:
    n = int(sys.stdin.readline().strip())
    pivot = 3**n
    string = ["-" for _ in range(pivot)]
    canto(0, pivot)
    print(''.join(map(str, string)))
  except:
    break
