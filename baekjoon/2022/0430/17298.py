# 오큰수
# https://www.acmicpc.net/problem/17298

# import sys
# sys.stdin = open('python/baekjoon/input2.txt','r')
# # input = sys.stdin.readline()
# stack1 = list(input().strip())
# N = int(input())

# 입력값 찾기 개빡치네 진짜
# 오른쪽에 있으면서 큰수를 찾아서 그 수로 바꾸기.
# 가장큰수 일경우 -1
 
# JS로 풀었을때 이중 for 로 풀게되면 배열크기가 커서 못풀었던것이 생각나서 for는 한번만 쓰자.

# n 만큼 배열을 만드는데 그 안에는 -1 로 채워져 있게 만들기. [초기값을 -1로 만든다]
# A 배열안에 있는 수 하나씩 꺼내서 탐색하는데
# while 문으로 전체 탐색.

# q를 만들고 큐에는 A에 인덱스 값만 저장(i)
# 큐에 마지막 인댁스 값에 해당하는 A의 숫자와 A[i] 번째 숫자와 비교
# A[i] 가 오큰수라면 stack에 들어있던 숫자 바꾸기(-1)

# 스택과 큐로 푸는문제인데 큐를 쓰면 더 빠르다고해서 큐를 썻는데 시간은 같아씀.
import sys
sys.stdin = open('python/baekjoon/input2.txt','r')
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
# print(N)
# print(A)
stack1 = [-1] * N # answer
stack = []

for i in range(N):
    while stack:
        if A[i] > A[stack[-1]]:
            stack1[stack.pop()] = A[i]
        else:
            break
    stack.append(i)
    

# print(' '.join(str(s) for s in stack))
print(' '.join(map(str, stack1)))





from collections import deque
import sys
sys.stdin = open('python/baekjoon/input2.txt','r')
# print(sys.stdin)
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
stack = [-1] * N
q = deque()

for i in range(N):
    while q:
        if A[i] > A[q[-1]]:
            stack[q.pop()] = A[i]
        else:
            break
    q.append(i)

print(' '.join(map(str, stack)))


# for i in range(N):
#     if A[i] > A[stack1[-1]]:
#         print(stack1[stack.pop()])


# 스택하나 더 필요 stack은 answer로 사용하고.
# stack = [-1] * N
# for _ in range(N):
#     while stack and stack[len(stack)-1][0] < A[i]:  # &&
    # .append(_)