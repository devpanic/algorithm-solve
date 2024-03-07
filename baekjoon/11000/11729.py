import sys
n = int(sys.stdin.readline().strip())

def hanoi(n, start, target, end):
    if n == 1:
        print(start, target)
        return
    
    hanoi(n - 1, start, end, target)
    print(start, target)
    hanoi(n - 1, end, target, start)
    

print(2 ** n - 1)
hanoi(n, 1, 3, 2)