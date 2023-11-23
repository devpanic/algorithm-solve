import sys

def convert_ascii(to_convert):
    return ord(to_convert) - 65

input_word = sys.stdin.readline()[0:-1]
length_word = len(input_word)
result_list = [0] * 26

for i in range(length_word):
    to_upper = length_word[i].upper()
    result_list[convert_ascii(to_upper)] += 1

print(max(result_list))
