# 괄호
# https://www.acmicpc.net/problem/9012

# from inspect import stack
# import sys
# input = open('python/baekjoon/input2.txt','r')
# T = int(input.readline())
# # T = int(input)

# for _ in range(T):
#     a = input.readline().rstrip()
#     # a = sys.stdin.readline().rstrip()
#     # print(a)
#     left = a.count('(')
#     right = a.count(')')
#     # print(left,right)
#     if left == right:
#         print("YES")
#     else:
#         print("NO")

# 제출
# import sys
# # input = open('python/baekjoon/input2.txt','r')
# T = int(input())

# for _ in range(T):
#     a = sys.stdin.readline().rstrip()
#     left = a.count('(')
#     right = a.count(')')
#     if left == right:
#         print("YES")
#     else:
#         print("NO")
        
        # 틀림. ())(() 이러면 틀림
        # 스택으로 풀자


import sys
input = open('python/baekjoon/input2.txt','r')
T = int(input.readline())
# T = int(input)

for _ in range(T):
    a = input.readline().rstrip() # 괄호들
    # a = sys.stdin.readline().rstrip()
    stack = []
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(a[i])
        elif a[i] == ')' and '(' not in stack:
            stack.append(a[i])
        elif a[i] ==')':
            stack.pop()
    if len(stack) ==0:
        print("YES")
    else:
        print("NO")
    # print(stack)

# 제출
import sys
T = int(input())

for _ in range(T):
    a = sys.stdin.readline().rstrip()
    stack = []
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(a[i])
        elif a[i] == ')' and '(' not in stack:
            stack.append(a[i])
        elif a[i] ==')':
            stack.pop()
    if len(stack) ==0:
        print("YES")
    else:
        print("NO")