# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# K번째수

def solution(array, commands):
    answer = []
    temp = []
    for command in commands:
        temp = array[command[0] - 1:command[1]];
        temp.sort();
        answer.append(temp[command[2] - 1]);
    return answer