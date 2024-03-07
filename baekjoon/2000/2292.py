import sys

input_data = int(sys.stdin.readline().rstrip())
cur_floor = 1
cur_room = 1

while True:
    if input_data <= cur_room :
        print(cur_floor)
        break
    cur_room = cur_room + cur_floor * 6
    cur_floor += 1