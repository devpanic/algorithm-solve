import sys

count, cut_line = map(int, sys.stdin.readline().split())
input = list(map(int, sys.stdin.readline().split()))
input.sort()
print(input[-cut_line])