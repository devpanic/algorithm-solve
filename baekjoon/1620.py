# 1620.py
import sys
n, m = map(int, sys.stdin.readline().split())
name_set = {}
num_set = {}

for i in range(1, n+1):
    pokemon = sys.stdin.readline().strip()
    name_set[pokemon] = i
    num_set[i] = pokemon

for _ in range(m):
    input = sys.stdin.readline().strip()
    if input in name_set:
        print(name_set[input])
    else:
        if int(input) in num_set:
            print(num_set[int(input)])