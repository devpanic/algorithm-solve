import sys
from collections import deque

queuestack_count = int(sys.stdin.readline().strip())
is_queue_or_stack = list(map(int, sys.stdin.readline().split()))
queuestack = deque()
initial_queuestack = list(map(int, sys.stdin.readline().split()))

insert_data_count = int(sys.stdin.readline().strip())
insert_data = list(map(int, sys.stdin.readline().split()))

for i in range(queuestack_count):
    if is_queue_or_stack[i] == 0:
        queuestack.appendleft(initial_queuestack[i])

for i in range(insert_data_count):
    queuestack.append(insert_data[i])
    print(queuestack.popleft(), end=" ")

# queuestack 동작에 있어 stack은 어떤 영향도 끼치지 않는다
# 다만 queue에서 도출되는 데이터를 어떻게 이용할지도 고민해야 시간 복잡도를 만족하며 정답을 낼 수 있는 문제였다.