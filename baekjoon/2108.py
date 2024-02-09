import sys

size = int(sys.stdin.readline())
data = []
sum = 0
max = -4001
min = 4001
max_count = 1
counts = {}
counts_result = []

for _ in range(size):
    input = int(sys.stdin.readline().strip())

    data.append(input)
    
    sum += input
    
    if input > max:
        max = input
    if input < min:
        min = input
    
    if input not in counts:
        counts[input] = 1
    else:
        temp = counts[input] + 1
        counts[input] = temp
        if max_count < temp:
            max_count = temp

data.sort()

for i, count in counts.items():
    if count == max_count:
        counts_result.append(i)
counts_result.sort()
print(round(sum / size))
print(data[int(size/2)])
if len(counts_result) > 1:
    print(counts_result[1])
else:
    print(counts_result[0])
print(max-min)