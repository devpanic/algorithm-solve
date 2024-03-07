import sys

def convert_to_standard(int_to_convert):
    if int_to_convert >= 10:
        return chr(int_to_convert + 55)
    else:
        return str(int_to_convert)

to_convert, system_standard = map(int, sys.stdin.readline().split())
result = ''

div = to_convert
rest = 0

while div > 0:
    rest = div % system_standard
    div = div // system_standard
    result += convert_to_standard(rest)
    
for i in range(len(result) - 1, -1, -1):
    print(result[i], end="")