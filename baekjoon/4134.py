# 4134번 다음 소수
# 정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오
# 0과 1은 소수가 아니기 때문에 2를 출력해야함
import sys

test_count = int(sys.stdin.readline())

for _ in range(test_count):
  input = int(sys.stdin.readline())
  if input < 3:
    print(2)
    continue
  else:
    num_gap = 2
    while input > -1:  # input이 유효
      prime_flag = True

      if input % 2 == 0:  # 짝수는 소수가 아님
        input += 1
      else:
        maximum = int(input**(1 / 2)) + 1
        for i in range(3, maximum, 2):
          if input % i == 0:
            input += num_gap
            prime_flag = False
            break
        if prime_flag:
          print(input)
          input = -1
