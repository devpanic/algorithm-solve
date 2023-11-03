# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse = True)
    answer = ''
    for number in numbers:
        answer += number
        
    if answer[0] == "0":
        return "0"
    else:
        return answer