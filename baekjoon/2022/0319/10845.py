# 큐
# https://www.acmicpc.net/problem/10845

# 명령은 총 여섯 가지이다.
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 
#           만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 
#           만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 
#           만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 제출용
from collections import deque
import sys
T = int(sys.stdin.readline())
queue = deque()
for i in range(T):
    command = sys.stdin.readline().rstrip().split(' ')
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else: print(0)
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else: print(queue[0])
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else: print(queue[-1])

# 확인용
# from collections import deque
# input = open('python/baekjoon/input2.txt','r')
# T = int(input.readline())
# queue = deque()
# for i in range(T):
#     command = input.readline().rstrip().split(' ')
#     # 입력값 확인 OK
#     if command[0] == 'push':
#         queue.append(command[1])

#     elif command[0] == 'pop':
#         if not queue:
#             print(-1)
#         else:
#             print(queue.popleft())
#     elif command[0] == 'size':
#         print(len(queue))
#     elif command[0] == 'empty':
#         if not queue:
#             print(1)
#         else: print(0)

#     elif command[0] == 'front':
#         if not queue:
#             print(-1)
#         else: print(queue[0])
#     elif command[0] == 'back':
#         if not queue:
#             print(-1)
#         else: print(queue[-1])
# print(queue)
