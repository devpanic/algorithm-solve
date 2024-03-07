import sys

coin_set = [25, 10, 5, 1]

order_count = int(sys.stdin.readline().rstrip())

for _ in range(order_count):
    cur_order = int(sys.stdin.readline().rstrip())
    for i in range(4):
        print(cur_order // coin_set[i], end=' ')
        cur_order = cur_order % coin_set[i]
