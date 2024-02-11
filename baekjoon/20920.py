import sys

count, length = map(int, sys.stdin.readline().split())
data = []
data_dic = {}

for _ in range(count):
    temp = sys.stdin.readline().strip()
    if len(temp) >= length:
        data.append(temp)

for word in data:
    if word in data_dic:
        data_dic[word][0] += 1
    else:
        data_dic[word] = [1, len(word)]

data_dic = sorted(data_dic.items(), key = lambda x: (-x[1][0], -x[1][1], x[0]))

for word, counts in data_dic:
    print(word)