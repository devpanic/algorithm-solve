import sys

num_list = []

for i in range(10):
    input = int(sys.stdin.readline())
    div_result = input % 42
    if num_list.count(div_result) == 0:
        num_list.append(div_result)

print(len(num_list))