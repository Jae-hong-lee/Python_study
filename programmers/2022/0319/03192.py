# 괄호 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/76502
# 무조건 다 짝이 맞아야 올바른 괄호이다.

def solution(s):
    answer = []
    cnt = 0
    for i in range(len(s)):
        stack = []
        for j in s:
            if j == '{'or j=='[' or j=='(':
                stack.append(j)
            # Exception has occurred: IndexError
            # list index out of range
            elif len (stack) > 0:
                if stack[-1] == '{' and j =='}':
                    stack.pop()
                elif stack[-1] == '[' and j ==']' :
                    stack.pop()
                elif stack[-1] == '(' and j ==')' :
                    stack.pop()
            else:
                stack.append(j)
        if len(stack)== 0: cnt+=1

        x = s[0]
        s = s[1:]+x
    
    return cnt
print(solution("[](){}")) # result 3
print(solution("[)(]"))   # result 0    
# 통과 ㅠㅠ

# def solution(s):
#     answer = []
#     cnt = 0
#     # x=s[0]
#     # s=s[1:]+x
#     # print(s)
#     for i in range(len(s)):
#         stack = []
#         for j in s:
#             if j == '{'or j=='[' or j=='(':
#                 stack.append(j)
#             # Exception has occurred: IndexError
#             # list index out of range
#             elif stack[-1] == '{' and j =='}':
#                 stack.pop()
#             elif stack[-1] == '[' and j ==']':
#                 stack.pop()
#             elif stack[-1] == '(' and j ==')':
#                 stack.pop()
        
#         if len(stack)== 0: cnt+=1

#         x = s[0]
#         s = s[1:]+x
#         # 뒤로 돌리고
#     answer.append(cnt)
#     return answer

# print(solution("[](){}")) # result 3
# print(solution("[)(]"))   # result 0     

# cnt 를 어디서 추가 시켜야할까, s 슬라이싱해서 뒤로 보내기.
# def solution(s):
#     answer = []
#     cnt = 0
#     s_list = list(s)
#     # print(s_list)
#     for i in range(len(s)):
#         stack = []
#         # cnt +=1
#         # 스택 초기화O ,돌리는것. X
#         for j in s:
#             if j == '{'or '[' or'(':
#                 stack.append(j)
#             # 스택에 열린 괄호들 이면 넣고 비교하기
#             if stack[-1] == '{' and j =='}':
#                 stack.pop()
#             if stack[-1] == '[' and j ==']':
#                 stack.pop()
#             if stack[-1] == '(' and j ==')':
#                 stack.pop()
#         # answer.append(cnt)
#         # cnt =0
#         # stack 값이 있는지 확인.
#         if not stack:
#             True
#         else: False
#     return answer

# print(solution("[](){}")) # result 3
# print(solution("[)(]"))   # result 0        


    # for i in range(len(s)): # 괄호를 한바퀴 도는것, 뒤로 추가 시켜줘야함.
    #     if s[i] == '(' or '[' or '{':
    #         answer.append(s[i])
    #     elif s[i] == ')' or ']' or '}' not in answer:
    #         answer.append(s[i])
    #     elif s[i] == ')' or ']' or '}':
    #         answer.pop()

    # if len(answer) == 0:
    #     return answer     # 0
    # else:
    #     return answer     # 0
