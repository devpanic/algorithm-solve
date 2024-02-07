# 25192.py
import sys

count = int(sys.stdin.readline())
members = set()
result = 0

for _ in range(count):
  str = sys.stdin.readline().strip()
  if str == "ENTER":
    result += len(members)
    members = set()
  else:
    members.add(str)

result += len(members)
# members.remove("ENTER")
print(result)
