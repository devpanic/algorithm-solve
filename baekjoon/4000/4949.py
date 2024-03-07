# match -> 336ms
while True :
    sentence = input()
    stack = []

    if sentence == "." :
        break

    for word in sentence :
        match word:
            case '(':
                stack.append(word)
            case '[':
                stack.append(word)
            case ')':
                if len(stack) != 0 and stack[-1] == '(' :
                    stack.pop()
                else :
                    stack.append(')')
                    break
            case ']':
                if len(stack) != 0 and stack[-1] == '[' :
                    stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
                else : 
                    stack.append(']')
                    break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')

# if -> 352ms
# while True :
#     sentence = input()
#     stack = []

#     if sentence == "." :
#         break

#     for word in sentence :
#         if word == '[' or word == '(' :
#             stack.append(word)
#         elif word == ']' :
#             if len(stack) != 0 and stack[-1] == '[' :
#                 stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
#             else : 
#                 stack.append(']')
#                 break
#         elif word == ')' :
#             if len(stack) != 0 and stack[-1] == '(' :
#                 stack.pop()
#             else :
#                 stack.append(')')
#                 break
#     if len(stack) == 0 :
#         print('yes')
#     else :
#         print('no')

# 4949 아래는 이전의 풀이, 괄호 짝 사이의 균형을 맞춰주는 부분이 풀리지 않아 스택을 이용한 풀이를 참조했다.
# import sys

# while True:
#     edge_count = 0
#     round_count = 0
#     input_sentences = list(sys.stdin.readline().split('.'))[0:-1]

#     if len(input_sentences[-1]) == 0:
#         break

#     for sentence in input_sentences:
#         current_sentence = list(sentence.split())

#         for curr_char in current_sentence:
#             print(curr_char)
#             match curr_char:
#                 case '[':
#                     edge_count += 1
#                 case ']':
#                     edge_count -= 1
#                 case '(':
#                     round_count += 1
#                 case ')':
#                     round_count -= 1
#             if edge_count < 0 or round_count < 0:
#                 break

#         if edge_count != 0 or round_count != 0:
#             print("no")
#         else:
#             print("yes")