import sys

def get_points_of_line(count):
    num_square = 2 ** count
    return num_square + 1

num_count = int(sys.stdin.readline().rstrip())
result = get_points_of_line(num_count)

print(result ** 2)