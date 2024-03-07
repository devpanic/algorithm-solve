import sys

n, m = map(int, sys.stdin.readline().split())
num_baskets = [i for i in range(n + 1)]
temp = -1

for _ in range(m):
    from_basket, to_basket = map(int, sys.stdin.readline().split())
    temp = num_baskets[from_basket]
    num_baskets[from_basket] = num_baskets[to_basket]
    num_baskets[to_basket] = temp

for i in range(1, n + 1):
    print(num_baskets[i], "", end='')
print("")