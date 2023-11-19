import sys

chess_tobe = [1, 1, 2, 2, 2, 8]
chess_list = list(map(int, sys.stdin.readline().split()))

for i in range(len(chess_list)):
    print(chess_tobe[i] - chess_list[i], end=" ")
print("")