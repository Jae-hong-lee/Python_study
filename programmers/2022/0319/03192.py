# 괄호 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/76502
# 무조건 다 짝이 맞아야 올바른 괄호이다.

def solution(s):
    answer = []
    # cnt = 0
    s_list = list(s)
    # print(s_list)
    for i in range(len(s)):
        stack = []
        # 스택 초기화O ,돌리는것. X
        for j in range(len(s)):
            if not stack: 
                stack.append(s_list[j])
            else:
                if stack[-1] == '(' :
                    stack.pop()
    return answer

print(solution("[](){}")) # result 3
print(solution("[)(]"))   # result 0        


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
