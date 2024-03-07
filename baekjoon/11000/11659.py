import sys

num_count, instruction_count = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
instructions = []
sums = [0]
current_sum = 0

for _ in range(instruction_count):
    instructions.append(list(map(int, sys.stdin.readline().split())))

for num in nums:
    current_sum += num
    sums.append(current_sum)

for instruction in instructions:
    print(sums[instruction[1]] - sums[instruction[0] - 1])