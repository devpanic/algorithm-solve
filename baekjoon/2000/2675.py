import sys

num_case = int(sys.stdin.readline())

for k in range(num_case):
    input_repeat_times, input_string = map(str, sys.stdin.readline().split())
    repeat_times = int(input_repeat_times)
    repeat_string = input_string

    for i in repeat_string:
        for j in range(repeat_times):
            print(i, end="", sep="")
    print("")