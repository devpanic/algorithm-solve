import sys

x_y_list = []

for _ in range(3):
    x_y_list.append(list(map(int, sys.stdin.readline().split())))

degree_list = []

for i in range(0, 3):
    x_degree = x_y_list[i][0] - x_y_list[i - 1][0]
    y_degree = x_y_list[i][1] - x_y_list[i - 1][1]
    if x_degree != 0 and y_degree != 0:
        degree_list.append(y_degree / x_degree)
    elif y_degree == 0:
        degree_list.append(1)
    else:
        degree_list.append(0)

# if degree_list[0] == degree_list[1]:

# elif degree_list[1] == degree_list[2]:
# elif degree_list[2] == degree_list[0]:
    print(degree_list)