import sys

test_num = int(sys.stdin.readline())
for _ in range(test_num):
    input = sys.stdin.readline()
    print(input[0], input[len(input) - 2], sep = '')