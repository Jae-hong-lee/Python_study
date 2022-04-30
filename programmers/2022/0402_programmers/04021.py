# 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302
# 2차원 문자열 배열 places가 매개변수

# 1. 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
# 2. 거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
# 3. 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

# 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 
# P: 응시자 / O: 빈테이블 / X: 파티션

# places -> 각 행은 하나의 대기실 구조를 나타냄, 5개 대기실크기 모두 5*5

# 맨해튼거리
# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, 
# T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다.

# 파티션은 false >??? table , 응사자 는 True??
from collections import deque
D = ((-1,0), (1,0), (0,-1), (0,1)) 
# D값은 상하좌우 로 움직이게 하기 위해서 지정
# 바뀔일은 없으니까 튜플로 지정했다.
def bfs(place, row, col):
    visited = [[False for _ in range(5)]for _ in range(5)]
    q = deque()
    visited[row][col] = True
    q.append(row,col,0) #시작 위치라 0
    # q에 넣어야할 값은 행렬좌표 그리고 거리이다. 3가지(행,열,거리)

    while not q.empty(): # 큐가 없을때까지
        curr = q.popleft() #디큐
        #거리가 2 이상 이면 확인할 필요가 없다 거리두기를 지키고 있어서
        if curr[2] > 2:
            continue # 컨티뉴로 스킵해서 넘겨버림
        if curr[2] != 0 and place[curr[0]][curr[1]] == 'P': 
            #2이하 거리에서 응시자 만날경우 근데 자기자신을 만날 경우도 있기 때문에 자기자신도 지워준다.
            return False #거리두기 지켜지지 않음 거리 2이하 거리에 응시자가 있다.
        
        for i in range(4):
            new_row = curr[0] + D[i][0]
            new_col = curr[1] + D[i][1]
            # 이제 4방향으로 탐색 현위치값에서 위에서 지정해준 D를 통해 상하좌우 좌표를 더해줌
            # 새로운 행열좌표. 좌표구간을 벗어날경우 제외
            if new_row < 0 or new_row >4 or new_col <0 or new_col>4:
                continue # 넘어갈경우 컨티뉴로 스킵
            if visited[new_row][new_col]:
                continue # 새로운 좌표가 이미 visited 한적 있다면 스킵
            # 파티션이 있을경우!!!! 
            if place[new_row][new_col] == 'X':
                continue 
            
            # 이제 이동할 수 있는 경우니까 마킹하고 인큐!
            visited[new_row][new_col] = True
            q = q.append((new_row,new_col,curr[2]+1))
        #이제 다음턴에서 다시 디큐 되면서 턴을 지나게 됨

def check(place):
    # 각각의 문자값을 확인
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if bfs(place, r, c) == False:
                    return False
                # 더 이상 탐색 이유 없음
    return True # 거리두기 지키고 있는 경우
# 다른 응시자 만나면 False

def solution(places):
    answer = []

    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer



print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# result [1,0,1,1,1]


from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(place, x, y):
    visited = [[False] * 5 for _ in range(5)]
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    while q:
        x, y, cost = q.popleft()
        if cost == 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny]:
                    continue
                if place[nx][ny] == 'P':
                    return False
                if place[nx][ny] == 'O':
                    q.append((nx, ny, cost + 1))
                    visited[nx][ny] = True
    return True

def solution(places):
    answer = []
    for place in places:
        p = [list(place[i]) for i in range(5)]	# 대기실
        flag = True
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    if not bfs(p, i, j):  # 거리두기 안 지켰을 경우
                        flag = False
            if not flag:
                break
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer
# 'P'인 곳에서부터 2만큼 떨어진 곳까지만 확인해 주면 되므로 BFS로 풀면 될 것이라 판단했다. 생각한 알고리즘은 아래와 같다.

# 대기실마다 확인하면서 'P'인 곳에서 bfs를 호출한다.
# bfs 내에서 좌표 및 거리 (x, y, cost)를 큐에 넣는다.
# 2-1. 거리가 2 미만이고 다음 방문할 곳이 'O'라면 큐에 넣는다.
# 2-2. 거리가 2 미만이고 다음 방문할 곳이 'P'라면 False를 리턴한다.
# 2-3. 거리가 2 면 중지한다.






# from collections import deque
# def BFS(word,row,col):
#     graph = [[0 for _ in range(5)] for _ in range(5)]
#     q = deque()
#     q.append(row,col,place)# q.append(현쟈위치) row,col q.append(row,col)
#     graph[row][col] = 1 #방문처리
#     while q:
#         v = q.popleft()
#         if v not in graph:
#             # graph.append(v)
#             graph[row][col] = 1
#             # 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#             for i in graph[v]:
#                 if not graph[i]:
#                     queue.append(i)
#                     graph[i] = True
#     # BFS 어렵다..
# def solution(places):
#     answer = []
#     for place in places:
#         for i in range(5):
#             for j in range(5):
#                 if place[i][j] =='P':
#                     if BFS(place[i][j],i,j):
#                         answer.append(1)
#                     else:
#                         answer.append(0)
#     return answer

# print(solution([
# ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
# ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
# ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
# ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
# ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# result [1,0,1,1,1]



# def BFS():
#     BFS
#     # BFS 만들자.
#     # 첫번째 행 기준 bfs(row =0, col = 0, place = P)

# def solution(places):
#     answer = []
#     for place in places:
#         # print(place)
#         for i in range(5):
#             for j in range(5):
#                 # answer.append(place[i][j])
#                 # 한글자씩 출력완료.
#                 # 응시자(P)찾기
#                 if place[i][j] =='P':
#                        # answer.append(BFS)
#                        # print(BFS)
#                     if BFS(i,j):
#                         answer.append(1)
#                     else:
#                         answer.append(0)
#                     # BFS true false로 출력
#     return answer

# print(solution([
# ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
# ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
# ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
# ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
# ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# # result [1,0,1,1,1]


# def BFS():
#     BFS
#     # BFS 만들자.
#     # 첫번째 행 기준 bfs(row =0, col = 0, place = P)

# def solution(places):
#     answer = []
#     for place in places:
#         # print(place)
#         for i in range(5):
#             for j in range(5):
#                 answer.append(place[i][j])

#                 # 한글자씩 출력완료.


#     return answer
