# 10816.py
import sys

have_count = int(sys.stdin.readline())
have_list = list(map(int, sys.stdin.readline().split()))
exist_count = int(sys.stdin.readline())
exist_list = list(map(int, sys.stdin.readline().split()))
have_map = {}

# 가지고 있는 카드들의 counter 정보 생성
for card in have_list:
  if card in have_map:
    curr_count = have_map[card]
    curr_count += 1
    have_map[card] = curr_count
  else:
    have_map[card] = 1

for i in range(exist_count):
  if exist_list[i] in have_map:  # key가 딕셔너리 안에 존재하면 count 출력
    print(have_map[exist_list[i]], end=" ")
  else:  # key가 딕셔너리 안에 존재하지 않으면 0 출력
    print(0, end=" ")
