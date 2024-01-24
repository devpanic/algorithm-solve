# 1991 트리 순회
# ref : https://velog.io/@ohk9134/백준-1991번-트리-순회-python-트리-구현
import sys

# 트리를 딕셔너리로 구현
# 노드 1개 = 리스트 요소 1개
# 왼쪽, 오른쪽 노드 = 배열의 각 인덱스 별 0, 1 인덱스의 요소
# 노드 정보가 항상 순차적으로 들어온다는 보장이 잇나?

node_sum = int(sys.stdin.readline())
tree = {}

for _ in range(node_sum):
  root, left, right = sys.stdin.readline().split()
  tree[root] = [left, right]


def preorder(start):
  print(start, end="")
  if tree[start][0] != ".":  # left 노드가 있으면
    preorder(tree[start][0])
  if tree[start][1] != ".":
    preorder(tree[start][1])


def inorder(start):
  if tree[start][0] != ".":  # left 노드가 있으면
    inorder(tree[start][0])
  print(start, end="")
  if tree[start][1] != ".":
    inorder(tree[start][1])


def postorder(start):
  if tree[start][0] != ".":  # left 노드가 있으면
    postorder(tree[start][0])
  if tree[start][1] != ".":
    postorder(tree[start][1])
  print(start, end="")


preorder('A')
print()
inorder('A')
print()
postorder('A')