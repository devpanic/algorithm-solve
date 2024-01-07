import sys
from collections import deque

def get_third_number(numbers, count):
    for _ in range(count):
        replace_number = numbers.popleft()
        numbers.append(replace_number)
    return numbers.popleft()

data_count, rotate_data = map(int, sys.stdin.readline().split())
numbers = deque()
result = []
current_index = 0

for i in range(1, data_count + 1):
    numbers.append(i)

for _ in range(data_count):
    result.append(get_third_number(numbers, rotate_data - 1))

print("<", end="")
for i in range(data_count - 1):
    print(result[i], ", ", sep="", end="")
print(result[data_count-1], ">", sep="")
