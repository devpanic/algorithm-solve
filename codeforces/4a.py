import sys

input = int(sys.stdin.readline().strip())

if input < 3:
  print("NO")
  exit()
if input % 2 == 0:
  print("YES")
else:
  print("NO")
