import sys

dial = [[],[],["A", "B", "C"], ["D","E","F"], ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"]
        , ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]]

to_call = list(map(str, sys.stdin.readline()))[0:-1]
result = 0

for call_number in to_call:
    for i in dial:
        for j in i:
        #     print(to_call, j)
            if call_number == j:
                result += dial.index(i) + 1;

print(result)