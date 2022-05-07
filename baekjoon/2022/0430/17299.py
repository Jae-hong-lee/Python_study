# 오등큰수
# https://www.acmicpc.net/problem/17299

# Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 
# 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 
# 그러한 수가 없는 경우에 오등큰수는 -1이다.

# 오큰수 풀이에 딕셔너리 추가해서 Ai 별로 개수세서 딕셔너리로 만들고 (1:3개..)  # 횟수 세는 부분 만들어야함.
# 딕셔너리 = count
# count에서 인댁스값 찾아서 answer 바꾸기.
# count(A[i]) > count(A[q[-1]]) 이런식??
# 값을 재할당하는 부분도 비슷하게 짜면될듯.

from collections import deque
import sys
sys.stdin = open('python/baekjoon/input2.txt','r')
N = int(input())
A = list(map(int, sys.stdin.readline().split()))

# A[i] 횟수 count에 넣어놓기.
count = {}
for j in A:
    if j not in count:
        count[j] = 1
    else:
        count[j] +=1

#오큰수 식 변화.

# 변환실패
q = deque()
answer = [-1] * N
for i in range(N):
    while q:
        if count[A[i]] > A[q[-1]]:
            # ???
            answer[q.pop()] = count[i]
            # break
        else: break
    q.append(i)
print(answer)

# from collections import deque
# import sys
# sys.stdin = open('python/baekjoon/input2.txt','r')
# N = int(input())
# A = list(map(int, sys.stdin.readline().split()))
# answer = [-1] * N
# q = deque()

# for i in range(N):
#     while q:
#         if A[i] > A[q[-1]]:
#             answer[q.pop()] = A[i]
#         else:
#             break
#     q.append(i)

# print(' '.join(map(str, answer)))
