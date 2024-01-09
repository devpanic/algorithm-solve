import sys
from collections import deque

data_count = int(sys.stdin.readline().rstrip())
input_data = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
result = []

for i in range(data_count):
    current_balloon = input_data.popleft()
    print(current_balloon[0], end=" ")
    if current_balloon[1] > 0:
        input_data.rotate(-(current_balloon[1] - 1))
    else:
        input_data.rotate(-current_balloon[1])