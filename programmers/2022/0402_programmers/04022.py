# 양궁대회
# https://programmers.co.kr/learn/courses/30/lessons/92342

# k점을 여러 발 맞혀도 k점 보다 많은 점수를 가져가는 게 아니고 k점만 가져가는 것을 유의하세요. 
# 또한 a = b = 0 인 경우, 즉, 라이언과 어피치 모두 k점에 단 하나의 화살도 맞히지 못한 경우는 
# 어느 누구도 k점을 가져가지 않습니다.

# BFS DFS 점수 비교
# 라이언과 어피치의 최대점수차이
# https://ryu-e.tistory.com/112
# https://youtu.be/caGtdr3_nxs

# 시뮬레이션 그리디??;;;;
def solution(n, info):
    answer = []
    return answer

print(5,[2,1,1,1,0,0,0,0,0,0,0])    # result [0,2,2,0,1,0,0,0,0,0,0]
print(1,[1,0,0,0,0,0,0,0,0,0,0])   # result [-1]
print(9,[0,0,1,2,0,1,1,1,1,1,1])    # result [1,1,2,0,1,2,2,0,0,0,0]
print(10,[0,0,0,0,0,0,0,0,3,4,3])   # result [1,1,1,1,1,1,1,1,0,0,2]