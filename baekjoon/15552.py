import sys
test_num = int(sys.stdin.readline())

for i in range(test_num):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)