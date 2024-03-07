import sys

n, m = map(int, sys.stdin.readline().split())
result_list = [i for i in range(1, n + 1)]

for _ in range(m):
    from_basket, to_basket = map(int, sys.stdin.readline().split())
    # 0 - [to_basket - from_basket]
    temp_list = result_list[from_basket - 1:to_basket]
    for i in range(to_basket - from_basket + 1):
        result_list[to_basket - i - 1] = temp_list[i]

for element in result_list:
    print(element, "", end = '')
print("")
