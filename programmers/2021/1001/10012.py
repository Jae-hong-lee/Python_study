#다리를 지나는 트럭
#트럭 여러 대가 강을 가로지리는 일차선 다리를 정해진 순으로 건너려 한다.
#모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지.
#다리에는 트럭이 최대 bridge_length대 올라갈 수 있고,
#다리는 weight 이하까지의 무게를 견딜 수 있다.
#단, 다리에 완전히 오르지 않은 트럭의 무게는 무시.

#트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있다면.
#무게가 7,4,5,6kg 인 트럭이 순서대로 최단시간안에 다리를 건너려면 다음과 같이 건넘.
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     cnt = 0
#     a=[]
#     while True:    
#         x = truck_weights.pop(0)
#         if truck_weights ==[]:
#             cnt +=bridge_length
#             break
#         else:
#             if x+truck_weights[0] < weight:
#                 a.append(x)
#             else:
#                 a.append(0)
#             cnt +=1        
#     return answer
# print(solution(2,10,[7,4,5,6]))
# print(solution(100,100,[10]))
#다리길이가 정의가 안되어 있다.

# def solution(bridge_length, weight, truck_weights):
#     b = [0 for i in range(bridge_length)] #다리의 길이를 초기화 즉 길이만큼 0을 넣음
#     answer= 0
#     while True:
#         b.pop(0) #7이들어가기 위해서 하나를 pop
#         answer +=1 #카운트.
#         if len(truck_weights)>0 and sum(b)+truck_weights[0]<=weight:
#             #트럭숫자가 없으면 아래로 내려감.
#             #다리에 있는 트럭 + 갈려는 트럭 에 무게가 다리의 무게를 초과하지 않으면.
#             b.append(truck_weights.pop(0))
#             #다리에 트럭추가.
#         else:
#             b.append(0) #그렇지 않으면 0을 추가해줘서 다리길이 유지.
#         if len(truck_weights) ==0 and sum(b) ==0:
#             #무한루프 break 하는 조건문
#             break
# 
#     return answer
    
# print(solution(2,10,[7,4,5,6]))
# print(solution(100,100,[10]))
#92.9 테스트5만 통과 안댐
#질문하기에서 식을 참고했..

def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length 
    answer= 0
    while True:
        bridge.pop()
        answer +=1
        if len(truck_weights)>0 and sum(bridge)+truck_weights[0]<=weight:
            bridge.insert(0,truck_weights.pop(0))
        else:
            bridge.insert(0,0)
        if len(truck_weights) ==0 and sum(bridge) ==0:
            break
        
    return answer
    
print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
#92.9 테스트5만 통과 안댐
#pop(0) 의 문제가 아니다.
#pop 을 통해 뒤에 값을 지우고 insert 를 통해 앞에다가 값을 추가함
#그냥 앞뒤만 바뀐것뿐 pop(0) 쓰는 숫자를 줄여봄. 근데 아님.

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer
print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
#if 문 하나로 조건 두개 지워버림 무한루프도 안썻고.
#근데 웃긴건 이것도 5번 틀림 -> 변수명 길이차이

def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length
    
    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    
    return time
#찐막.
#while 문 차이?






#0 for i in range(bridge_length)
#[표현식 for 항목 in 반복가능객체 if 조건문]

#b는 배열 안에 배열들을 선언하는 게 아니라 각각 배열들을 선언
#a는 배열 안에 2차원 배열을 선언
#따라서 a 처럼 선언하고 2차원 배열에 값을 넣으면 2차원 좌표가 아니라 
#모든 배열이 동시에 같은 값을 넣게됨
#출력 해줄때 같은 것처럼 보이는데 전혀 다르다.
# a = [[0] * 2] * 3
# b = [[0] * 2 for _ in range(3)]

# a[0][0] = 1
# b[0][0] = 1

# print(a)
# print(b)

# # 출력
# [[1, 0], [1, 0], [1, 0]]
# [[1, 0], [0, 0], [0, 0]]