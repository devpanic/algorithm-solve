import sys

def square(count, num):
    if count == 0:
        return 1
    else:
        return num * square(count - 1, num)
    
def chr_to_int(chr):
    try:
        return int(chr)
    except:
        return ord(chr) - 55

input_data = list(map(str, sys.stdin.readline().split()))

to_convert = input_data[0]
len_to_convert = len(to_convert)
standard = int(input_data[1])
system_multiply_list = [[] for _ in range(len_to_convert)]
result = 0

for i in range(len_to_convert - 1, -1, -1):
    system_multiply_list[i] = square(len_to_convert - i - 1, standard)

for i in range(len_to_convert):
    result += system_multiply_list[i] * chr_to_int(to_convert[i])

print(result)