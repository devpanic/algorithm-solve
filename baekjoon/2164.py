import sys
from collections import deque

card_count = int(sys.stdin.readline().rstrip())
loop_count = card_count -1
card_set = deque()

for i in range(card_count):
    card_set.append(i + 1)

for _ in range(loop_count):
    card_set.popleft()
    replace_num = card_set.popleft()
    card_set.append(replace_num);

print(card_set[0])


# --------- use list ---------
# for i in range(card_count):
#     card_set.append(i + 1)

# for _ in range(loop_count):
#     card_set.pop(0)
#     change_num = card_set.pop(0)
#     card_set.append(change_num)
#     # print(card_set)

# print(card_set[0])

# ref : https://tooo1.tistory.com/88