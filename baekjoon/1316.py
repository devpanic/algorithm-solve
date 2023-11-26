import sys

num_strings = int(sys.stdin.readline()[0:-1])

string_list = []
result = 0

for _ in range(num_strings):
    string_list.append(sys.stdin.readline()[0:-1])

for current_string in string_list:
    before = current_string[0]
    exist_list = set()
    isConsecutive = 1

    for i in range(len(current_string)):
        if before != current_string[i]:
            if current_string[i] in exist_list:
                isConsecutive = 0
                break
            
        exist_list.add(current_string[i])
        before = current_string[i]

    result += isConsecutive

print(result)