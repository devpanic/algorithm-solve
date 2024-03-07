import sys

result = ["Equilateral", "Isosceles", "Scalene", "Error"]
input_degree = []

for _ in range(3):
    input_degree.append(int(sys.stdin.readline().rstrip()))

sum_degree = sum(input_degree)
scal_flag = False

if sum_degree != 180:
    print(result[3])
else:
    count1 = input_degree.count(input_degree[0])
    count2 = input_degree.count(input_degree[1])
    count3 = input_degree.count(input_degree[2])
    if count1 == 3:
        print(result[0])
    elif count1 == 2 or count2 == 2 or count3 == 2:
        print(result[1])
    else:
        print(result[2])