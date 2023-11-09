# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# H-Index

def solution(citations):
    citations.sort()
    cur_hIndex = 0

    while(True):
        if cur_hIndex < sum( citation > cur_hIndex for citation in citations ):
            cur_hIndex += 1        
        elif cur_hIndex >= sum( citation > cur_hIndex for citation in citations ):
            break;
            
    return cur_hIndex;