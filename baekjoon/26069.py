import sys

count = int(sys.stdin.readline())
is_chongchong = False
dancing = set()
for _ in range(count):
    n, m = sys.stdin.readline().split()
    if not is_chongchong:
        if n == "ChongChong" or m == "ChongChong":
            is_chongchong = True
            dancing.add(n)
            dancing.add(m)
    else:
        if n in dancing or m in dancing:
            dancing.add(n)
            dancing.add(m)

print(len(dancing))