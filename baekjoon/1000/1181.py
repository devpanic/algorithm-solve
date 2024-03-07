import sys

count = int(sys.stdin.readline())
result = []
word_dic = set()

for _ in range(count):
  word = sys.stdin.readline().strip()
  if word not in word_dic:
    word_dic.add(word)
    result.append([len(word), word])

result.sort()

for word in result:
  print(word[1])
