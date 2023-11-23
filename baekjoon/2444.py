import sys

number = int(sys.stdin.readline()[0:-1])
cur_count = 0

for i in range(1, number + 1):
    for j in range(number, 0, -1):
        if i * i >= j * j:
            print("*", end="")
            cur_count += 1
        else:
            print(" ", end="")
    for k in range(1, cur_count):
        print("*", end="")
    print("")
    cur_count = 0

for i in range(number):
    for j in range(number):
        if i * i >= j * j:
            print(" ", end="")
        else:
            print("*", end="")
            cur_count += 1
    for k in range(1, cur_count):
        print("*", end="")
    print("")
    cur_count = 0