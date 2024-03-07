import sys

result = ["Equilateral", "Isosceles", "Scalene", "Error"]

while True:
    try:
        input_data = list(map(int, sys.stdin.readline().split()))
        input_data.sort()

        if sum(input_data) == 0:
            break
        
        if input_data[2] >= input_data[0] + input_data[1]:
            print("Invalid")
            continue
        
        count_first = input_data.count(input_data[0])
        count_second = input_data.count(input_data[1])

        if count_first == 3:
            print(result[0])
        elif count_first == 2 or count_second == 2:
            print(result[1])
        else:
            print(result[2])
    except:
        break