# 에라토스테네스의 체 사용하기
# 현재 인덱스가 소수인지 확인하고 배수를 지워준다
# 내 로직이 통과는 되었는데 너무 너저분해서 다른걸 찾아봤다
# 여러 로직이 있었는데 아래 코드가 가장 에라토스테네스의 체를 요구사항대로 잘 구현한 것 같다.
# 아래의 코드로 수정하니 실행시간이 6060ms -> 592ms가 되었다
import sys

a, b = map(int, sys.stdin.readline().split())
dataset = [True for i in range(b + 1)]
dataset[0] = False
dataset[1] = False

for i in range(2, int(b ** (1/2)) + 1):    # 소수인지 확인하는 알고리즘
    if dataset[i] == True:
        j = 2 
        while i * j <= b:
            dataset[i * j] = False
            j += 1

for i in range(a, b + 1):
    if dataset[i] == True:
        print(i)

# 출처: https://mail-study.tistory.com/4 [매일공부:티스토리]