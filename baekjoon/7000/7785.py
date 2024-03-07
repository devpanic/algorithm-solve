# 7785.py
import sys

logs = int(sys.stdin.readline())
in_company = set()
result = []
for _ in range(logs):
  name, moving = sys.stdin.readline().split()
  if moving == "enter":
    in_company.add(name)
  else:
    in_company.remove(name)

while len(in_company) > 0:
  result.append(in_company.pop())

result.sort(reverse=True)

for name in result:
  print(name)
