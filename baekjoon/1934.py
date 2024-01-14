import sys

loop_count = int(sys.stdin.readline())

for _ in range(loop_count):
    a, b = map(int, sys.stdin.readline().split())
    
    origin_a = a
    origin_b = b

    # 최대공약수 - 유클리드 호제법
    while b > 0:
        a, b = b, a % b
    
    # 최소공배수 = 두 값의 곱 / 최대공약수
    print(int(origin_a * origin_b / a))