# 요세푸스 문제
# https://www.acmicpc.net/problem/1158

# 현재사람 리스트 만들고 K번째 인 사람 죽이기
# 죽이는건 계속 돌아가야하니까 -> while

# 제출용
# 제출할때 sys.stdin = 주석처리하기.
# 확인용
from collections import deque
import sys
sys.stdin = open('python/baekjoon/input2.txt','r')
input = sys.stdin.readline().split()
N = int(input[0])
K = int(input[1])
answer = "<"
arr = deque()
for i in range(1, N+1):
    arr.append(i)
# arr = [i for i in range(1,N+1)]
# 큐를 만들고 리스트로 만들어서 시간초과되서 오류가 난거다
# arr를 큐로 만들고 한문자한문자 추가해주니까 해결
count =1
while arr:
    num = arr.popleft()
    # arr를 큐로 만들고 리스트로 arr를 추가해서 popleft가 안먹혔던 것.
    if count ==K:
        answer += str(num) + ', '
        count = 0
    else:
        arr.append(num)
    count+=1
print(answer[0:len(answer)-2] + '>')

# 시간초과
# arr = [i for i in range(1,N+1)]
# print(arr) # [1, 2, 3, 4, 5, 6, 7]
# # 앉아 있는 사람들 배열
# answer = []
# stack = []

# count = 1
# while (len(arr) >0):
#     num = arr.pop(0)
#     if( count == K):
#         answer.append(num)
#         count = 0;
#     else:
#         arr.append(num)

#     count+=1
# # print(answer)


# # -> 어떻게 숫자형을 문자형응로 변경해서 괄호랑 같이출력?
# word = list(map(str,answer))
# print( "<",(', ').join(word), ">" ,sep = '')
#sep='' ->중복제거


# word =""
# for c in answer:
#     word += str(c) + ' '
# print(word)