# 시간초과 - main line 요소가 다 소비된 뒤 한번 더 sub line을 확인하기 위해 while문을 썼던게 요인이었던 것 같다.
# 논리를 압축해서 하나의 while로 바꾸니 정답이었다
import sys
from collections import deque

students = int(sys.stdin.readline().strip()) + 1

# 현재줄, 골목줄 모두 스택필요
main_line = list(map(int, sys.stdin.readline().split()))
main_line.reverse()
sub_line = deque()
curr_index = 1

if main_line[-1] != 1:
    sub_line.append(main_line.pop())

while curr_index != students:
    if main_line and main_line[-1] == curr_index:
        main_line.pop()
        curr_index += 1
    elif sub_line and sub_line[-1] == curr_index:
        sub_line.pop()
        curr_index += 1
    else:
        sub_line.append(main_line.pop())
        if not main_line or (len(sub_line) > 1 and sub_line[-1] > sub_line[-2]):
            curr_index = -1
            break
        

if curr_index != students:
    print("Sad")
else:
    print("Nice")
