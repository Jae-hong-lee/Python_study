# 쇠막대기
# https://www.acmicpc.net/problem/10799

# 쇠막대기를 레이저로 절단, 쇠막대기는 위 아래로 겹치고, 위에서 수직으로 레이져를 발사해서 절단함
# 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
    # 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
# 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

# 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
# 쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다. 

# 열린괄호일때 다음 괄호가 닫힌 괄호이다면, 레이져니까 자른다. stack의 길이만큼 count++
# 닫힌괄호가 아니라면 stack에 쌓기
# 닫힌 괄호만 나왔을 경우 stack pop으로 맨위에 값을 빼고 count+1

# 런타임에러(indexError)
import sys
sys.stdin = open('python/baekjoon/input2.txt','r')
input = list(sys.stdin.readline())
stack = []
count = 0

for i in range(len(input)):
    if input[i] == '(': 
        stack.append(input[i])
    else:
        if input[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count +=1

print(count)

# 	런타임 에러 (FileNotFoundError)
# 조건식을 좀 더 가다듬어야 겠다. 내일.
# 오히려 다음날에 한 식이 indexError로 틀리고 첫날에 만들었던 코드가 통과되었다.
# 파이썬을 너무 오랜만에 다루다 보니까 sys.stdin 재할당한것을 주석처리를 안해서 생긴 오류였다. 
import sys
sys.stdin = open('python/baekjoon/input2.txt','r')
input = list(sys.stdin.readline())
# print(input) # 리스트 형태로 들어가진다. result 17이 출력되어야함
count = 0
stack = []

for i in range(len(input)):
    if input[i] == '(':
        if input[i+1] == ')': 
            count += len(stack)
        else: 
            stack.append(input[i])

    elif input[i] == ')':
        if input[i-1] != '(':
            stack.pop()
            count+=1
        
# print(stack)
print(count)
# for in xxxx
# for _ in input:
#     # print(_)
#     if _ === '(':
#         if 


#     else if _ === ')':