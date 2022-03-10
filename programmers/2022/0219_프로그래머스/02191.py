# 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978


# 마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때, 
# 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.


# def solution(N, road, K):
#     answer = 0

#     return answer
# print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)) # result 4
# ----------------------------------------
# BFS, DFS, 다익스트라 알고리즘 = 최단거리 찾기? 문제이다 라고 생각이듬.
# 
# 플로이드 워셜 알고리즘: 동작 과정.
# https://freedeveloper.tistory.com/277?category=888096

def solution(N, road, K):
    answer = 0
    inf = int(1e9) # 무한. 10억 설정
    graph = [[]for i in range (N+1)] 
    visited = [False] * (N+1)  
    distance = [inf] * (N+1)
    

    for _ in (road): # 모든 간선 정보 입력받기
        node1, node2, dis = _   # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[node1].append((node2,dis))
    
    # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    def min_node():
        min_value = inf
        index = 0
        for i in range(1,N+1):
            if distance[i]<min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start): #다익스트라
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]

        for i in range(N-1):
            now = min_node()
            visited[now] = True
            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
        dijkstra(start)

    # print(graph)
    # print(distance)
    # print(visited)
    for i in range(1,N+1):
        if distance[i] == inf:
            return 'INFINITY'
        else:
            print(distance[i])
    return answer
# print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)) # result 4
# 다익스트라 알고리즘만 구현해보았다.
# [[], [(2, 1), (4, 2)], [(3, 3)], [], [], [(2, 2), (3, 1), (4, 2)]]
# 보기 처럼 1,2,5 는 들어갔는데 3,4는 값이 안들어 가져 있음
# 양방향성이라고함.
# 다익스트라 알고리즘 스타트 위치가 이상함, start 를 지정안해줌

# 두번째 시도. K를 활용해야함.
def solution(N, road, K):
    answer = 0
    inf = int(1e9) # 무한. 10억 설정
    graph = [[]for i in range (N+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
    visited = [False] * (N+1) # 방문한 적이 있는지 체크하는 목적의 리스트 
    distance = [inf] * (N+1) # 최단 거리 테이블 모두 무한으로 초기화
    

    for _ in road: # 모든 간선 정보 입력받기
        node1, node2, dis = _   # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[node1].append((node2,dis))
        graph[node2].append((node1,dis))
        # 양방향성
    
    # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    def min_node():
        min_value = inf
        index = 0 # 가장 최단 거리가 짧은 노드(Index)
        for i in range(1,N+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start): # 다익스트라
        distance[start] = 0 # 시작노드 초기화
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]
        # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복.

        for i in range(N-1):
            # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문.
            now = min_node()
            visited[now] = True
            # 현재 노드와 연결된 다른 노드 확인
            
            for j in graph[now]:
                cost = distance[now] + j[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 짧은 경우 업댓
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
    dijkstra(1) # 알고리즘 수행
    print(graph)
    print(distance)
    print(visited)
    # for d in distance: # distance 거리가 k 이하이거나 같을때 길이 출력.
    #     if d <= K:
    #         return len(d)
    for i in range(1,N+1):
        if distance[i] <=K:
            answer +=1
    return answer
# print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)) # result 4



# 세번째 시도. K를 활용해야함.
def solution(N, road, K):
    answer = 0
    inf = int(1e9) # 무한. 10억 설정
    graph = [[]for i in range (N+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
    visited = [False] * (N+1) # 방문한 적이 있는지 체크하는 목적의 리스트 
    distance = [inf] * (N+1) # 최단 거리 테이블 모두 무한으로 초기화
    

    for _ in road: # 모든 간선 정보 입력받기
        node1, node2, dis = _   # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[node1].append((node2,dis))
        graph[node2].append((node1,dis))
        # 양방향성
    
    def min_node():
        min_value = inf
        index = 0 # 가장 최단 거리가 짧은 노드(Index)
        for i in range(1,N+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start): # 다익스트라
        distance[start] = 0 # 시작노드 초기화
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]

        for i in range(N-1):
            now = min_node()
            visited[now] = True
            
            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
    dijkstra(start=1) 

    for i in range(1,N+1):
        if distance[i] <=K:
            answer +=1
    return answer
# print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)) # result 4
# 71.9점 : 9,15,19,21,24,25,27,28,29
# queue 를 활용해서 만들 수 있는 다익스트라 알고리즘을 활용해보자.





import heapq
def solution(N, road, K):
    answer = 0
    inf = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [inf] * (N+1)
    
    for _ in road: # 모든 간선 정보 입력받기
        node1, node2, dis = _   # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[node1].append((node2,dis))
        graph[node2].append((node1,dis))
        # 양방향성

    # 다익스트라 알고리즘 
    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))
        
        while q:
            # 최단거리 노드
            dist, now = heapq.heappop(q)
            # 이미 방문했거나 최솟값이 아닌 경우 
            if distance[now] < dist:
                continue 
            # 연결된 노드들에 대해 
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 정보보다 더 적은 시간이 필요한 경우 갱신
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    dijkstra(1) # 마을은 1부터 시작됨 0은 값이 없음
    # 1을 집어넣음 으로써 알고리즘 시작 될 때, start 부분을 0으로 초기화 하면서
    # 노드1 의 최단거리는 0임. 1부터 시작하니까.

    for i in range(1,N+1):
        if distance[i] <=K:
            answer +=1
    # K 이하의 시간에 배달이 가능한 마을의 개수 
    return answer
print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)) # result 4
 
#  참고자료
# https://www.youtube.com/watch?v=F-tkqjUiik0&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=30
# https://freedeveloper.tistory.com/384?category=888096