# 스택 수열
# https://www.acmicpc.net/problem/1874

# 수열이란? 수의 나열, 수의 규칙적 나열이기 때문에 일정한 규칙을 가지고 나열되어 있는 것
# 수의 규칙?
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

# 힌트
# 1부터 n까지에 수에 대해 차례로 
# [[push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 
# 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.
# 이런느낌인듯 # [[push(1), push(2), push(3), push(4), *pop(4), *pop(3), push(5), push(6), *pop(6)...] 
# pop된수는 제외하고 카운트하며 push?? 

# 제출용
# import sys
# T = int(sys.stdin.readline())


# 확인용
# sys.stdin = open('python/baekjoon/input2.txt','r')
# temp = list(map(int, input().split(' ')))
# T = temp[0]
# BLOCK = [int(input()) for _ in range(T)]
# for i in range(0, T):
#     BLOCK.append(int(input()))
# print(BLOCK) # 입력값 확인 OK

# 제출
# input -> sys.stdin.readline()
import sys
sys.stdin = open('python/baekjoon/input2.txt','r')
# input = sys.stdin.readline()
temp = list(map(int, input().split(' ')))
T = temp[0]
num = [int(input()) for _ in range(T)]

cnt = 1 # 카운트
stack =[] # 스택 
answer = [] # 출력값 저장
for i in range(T):
    while num[i] >= cnt:
        answer.append('+')
        stack.append(cnt)
        cnt +=1

    if stack[-1] == num[i]:
        stack.pop()
        answer.append('-')
    # else:             # 이쪽 부분 조건을 다시 세워야할듯.
    #     print("NO")  
    else:
        print("NO")
        exit(0) # 종료함수
        
for i in answer:
    print(i)

# 전에 풀었던 스택 문제 처럼 push(+) pop(-)이 있는것이 아닌 
# 어느 한 지점까지 + 해주고 그 지점에 도착하면 그 값을 - 
# 한번 나온 값들은 또 들어가진 않음. 초기화 x  -> *cnt를 세주자.


# 수도코드
# import sys
# sys.stdin = open('python/baekjoon/input2.txt','r')
# temp = list(map(int, input().split(' ')))
# T = temp[0]
# num = [int(input()) for _ in range(T)]

# cnt = 1 # 카운트
# stack =[] # 스택 , 임시저장
# answer = [] # 출력값 저장
# for i in range(T):
#     while num[i] >= cnt:
#         answer.append('+')
#         stack.append(cnt)
#         cnt +=1
#     # print(answer, stack)

#     if stack[-1] == num[i]:
#         stack.pop()
#         answer.append('-')
#     else:
#         print("NO")
        
#         # return "NO" # return 사용불가.
# # print(answer) # answer 값들 잘 들어감
# for i in answer:
#     print(i)
# 왜 else 로 안들어가냐??? 3에서 pop(-) 출력후 4 or 3는 어디로감?
# ㄴㄴ 들어가짐, 단지 밑에 answer 줄까지 내려가져서 +- 출력된거임






    # print(num)
    # 이 조건을 반복 시켜야함.
    # if num[i] >= cnt:
    #     cnt+=1
    #     answer.append('+')
    # else:
    #     1=0
    #     return print("NO")

# for i in answer:
#     print(i)
