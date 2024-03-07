import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().strip())
string = [["*" for _ in range(n)] for _ in range(n)]

def set_square(x, y, gap):
    if gap == 0:
        return
    for i in range(x + gap, x + 2 * gap):
        for j in range(y + gap, y + 2 * gap):
            string[i][j] = " "

    new_gap = gap // 3
    for i in range(x, x + 3 * gap, gap):
        for j in range(y, y + 3 * gap, gap):
            set_square(i, j, new_gap)
        
set_square(0, 0, n // 3)

for i in range(n):
    print(''.join(map(str, string[i])))