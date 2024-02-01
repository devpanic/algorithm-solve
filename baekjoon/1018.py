# ref : https://only-wanna.tistory.com/entry/%EB%B0%B1%EC%A4%80-1018%EB%B2%88-%EC%B2%B4%EC%8A%A4%ED%8C%90-%EB%8B%A4%EC%8B%9C-%EC%B9%A0%ED%95%98%EA%B8%B0
import sys
n, m = map(int, sys.stdin.readline().split())
data = []
result=[]
# 입력한 데이터를 리스트에 저장
for _ in range(n):    
    data.append(list(map(str, sys.stdin.readline().strip()))) 

# 리스트를 8*8로 쪼개기
for i in range(0, n-7):
    for j in range(0, m-7):
        count1 = 0        
        count2 = 0        
        # 8*8 보드를 하나씩 검사하기        
        for x in range(i, i+8):            
            for y in range(j, j+8):                
                # 인덱스 합이 짝수인 경우 일정한 색 가지게 됨.                
                if (x+y) % 2 == 0:                   
                    # 0,0 값이 B인 경우                   
                    if data[x][y] != 'W':                        
                        count1 += 1                    
                    # 0,0 값이 W인 경우                    
                    if data[x][y] != 'B':                        
                        count2 += 1                
                # 인덱스 합이 홀수인 경우 일정한 색               
                else:                    
                    # 0,0 값이 W인 경우                    
                    if data[x][y] != 'W':                        
                        count2 += 1                   
                    # 0,0 값이 B인 경우                    
                    if data[x][y] != 'B':                        
                        count1 += 1        
        result.append(count1)        
        result.append(count2) 

print(min(result))