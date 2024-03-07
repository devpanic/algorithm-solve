import sys

num_subject = int(sys.stdin.readline())
grades = list(map(int, sys.stdin.readline().split()))

most_rank = max(grades)
sum_rank = sum(grades)

print(sum_rank / most_rank * 100 / num_subject)