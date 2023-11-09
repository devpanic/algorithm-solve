import sys
dice_list = list(map(int, sys.stdin.readline().split()))

for dice in dice_list:
    if dice_list.count(dice) == 2:
        print(1000 + dice * 100)
        exit()
    elif dice_list.count(dice) == 3:
        print(10000 + dice * 1000)
        exit()
print(max(dice_list) * 100)