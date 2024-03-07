import sys
# from collections import deque

# def get_third_number(numbers, count):
#     for _ in range(count):
#         replace_number = numbers.popleft()
#         numbers.append(replace_number)
#     return numbers.popleft()

# data_count, rotate_data = map(int, sys.stdin.readline().split())
# numbers = deque()
# result = []
# current_index = 0

# for i in range(1, data_count + 1):
#     numbers.append(i)

# for _ in range(data_count):
#     result.append(get_third_number(numbers, rotate_data - 1))

# print("<", end="")
# for i in range(data_count - 1):
#     print(result[i], ", ", sep="", end="")
# print(result[data_count-1], ">", sep="")
# 위의 코드 실행시간 : 80ms, 아래의 코드 실행시간 : 40ms

# 제거해야 하는 노드의 인덱스를 구하는 아이디어
# 다음 인덱스 = (현재 노드 인덱스 + N(번째)) % 현재 무리 내 인원 수
n, k = map(int, input().split())
people = list(range(1, n + 1)) #둥글게 모여앉은 사람들
k_index = 0
result = []

for i in range(n): #n번만 반복하면 되니까
	k_index = (k_index + k - 1) % len(people)
	result.append(people.pop(k_index))
    
print('<' + str(result)[1:-1] + '>')

#ref : https://velog.io/@juyeonma9/%EB%B0%B1%EC%A4%80-1159-%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4%EB%AC%B8%EC%A0%9C-python
