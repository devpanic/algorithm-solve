import sys

n, m = map(int, sys.stdin.readline().split())
num_baskets = [0] * (n + 1)

for _ in range(m):
    from_basket, to_basket, which_ball = map(int, sys.stdin.readline().split())
    for i in range(from_basket, to_basket + 1):
        num_baskets[i] = which_ball

for i in range(1, n + 1):
    print(num_baskets[i], "", end='')
print("")