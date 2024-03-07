import sys

sum_predict = int(sys.stdin.readline())
num_things = int(sys.stdin.readline())
sum = 0
for i in range(num_things):
    a, b = map(int, sys.stdin.readline().split())
    sum += a * b

if sum != sum_predict : 
    print("No")
else:
    print("Yes")