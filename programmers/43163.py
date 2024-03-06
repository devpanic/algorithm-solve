def solution(begin, target, words):
    n = len(words)
    min = n + 1
    visited = [False for _ in range(len(words))]
    count = 0
    
    for i in range(n):
        if check(begin, words[i]):
            if target == words[i]:
                return 1
            count = dfs(words[i], target, i, words, visited, 1)
            if count < min:
                min = count
            count = 0
    
    if min > n:
        return 0
    else:
        return min
            
        
def dfs(begin, target, idx, words, visited, count):
    visited[idx] = True
    counts = [len(words) + 1]
    
    for i in range(len(words)):
        if (not visited[i]) and check(begin, words[i]):
            if words[i] == target:
                visited[idx] = False
                return count + 1
            
            counts.append(dfs(words[i], target, i, words, visited, count + 1))
            visited[i] = False
            
    return min(counts)
        
def check(word, temp_target):
    diff_count = 0
    
    for i in range(len(word)):
        if word[i] != temp_target[i]:
            diff_count += 1
        if diff_count > 1 :
            return False
        
    return True
    