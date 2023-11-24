import sys
import copy

def convert_ascii(to_convert):
    return ord(to_convert) - 65

def convert_int(to_convert):
    return chr(to_convert + 65)

input_word = sys.stdin.readline()[0:-1]
length_word = len(input_word)
result_list = [0] * 26

for i in range(length_word):
    to_upper = input_word[i].upper()
    result_list[convert_ascii(to_upper)] += 1

origin_list = copy.deepcopy(result_list)
result_list.sort(reverse=True)

if result_list[0] == result_list[1]:
    print("?")
else:
    print(convert_int(origin_list.index(max(origin_list))))
