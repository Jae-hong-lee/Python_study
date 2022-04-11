# n^2 배열 자르기
# 정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

# n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
# i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
# 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., 
# arr[right]만 남기고 나머지는 지웁니다.
# 정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진
# 1차원 배열을 return 하도록 solution 함수를 완성해주세요.


# answer[i] = Math.max(row, col);
# 사각형 채우기
def solution(n, left, right):
    answer = []
    graph = [[0] * n for a in range(n)]
    for i in range(n):
        for j in range(n):
            graph[i][j] = max(i,j)+1
    # print(graph)
    return answer
# print(solution(3,2,5)) #[3,2,2,3]
# max 를 생각하다니 대단한사람..

def solution(n, left, right):
    answer = []
    graph = [[0] * n for a in range(n)]
    for i in range(n):
        for j in range(n):
            graph[i][j] = max(i,j)+1
    answer = sum(graph,[])
    # 2차원 리스트 1차원으로
    return answer[left:right+1] # 슬라이싱
# print(solution(3,2,5)) #[3,2,2,3]

# 테스트 1 〉	통과 (81.99ms, 18MB)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	통과 (2.40ms, 10.3MB)
# 테스트 5 〉	통과 (2.00ms, 10.4MB)
# 테스트 6 〉	통과 (4114.87ms, 59.8MB)
# 테스트 7 〉	통과 (4978.36ms, 62.4MB)
# 테스트 8 〉	통과 (4005.20ms, 62.3MB)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	실패 (시간 초과)
# 테스트 13 〉	실패 (시간 초과)
# 테스트 14 〉	실패 (시간 초과)
# 테스트 15 〉	실패 (시간 초과)
# 테스트 16 〉	실패 (시간 초과)
# 테스트 17 〉	실패 (시간 초과)
# 테스트 18 〉	실패 (시간 초과)
# 테스트 19 〉	실패 (시간 초과)
# 테스트 20 〉	실패 (시간 초과)
# 합계 30점..?
# 이건 공식이 있다. 내가 할 수 있는 최선의 코드였던거 같은데 이건 공식이다.

# n의 범위가 10에7승 까지 있기 때문에 코드를 정말 빡빡하게 짜야 합니다.
# 문제에서 left와 right를 제시한 만큼 left 전 의미없는 값들과 right 후  
# 의미없는 값들은 아예 만들지 않고 스킵하는 방식으로 코드를 짜야 합니다. 

# 그리고 배열의 초반에 같은 값이 연속되는 경우가 많기 때문에 해당 값들은 for문 없이 배열로 만들고 
# 뒤의 연속적으로 증가하는 값만 for문으로 만들어 붙이는 방식이
# for문을 적게 돌기 때문에 시간을 아낄 수 있었습니다.
# 즉 수많은 값들 중 left와 right 사이의 값만 만들 수 있다면 최상의 코드고 
# 아무리 못해도 우리가 만들 값의 범위는
# 최대 (left - n) ~ (right + n) 사이의 값만 만들고 잘라야 시간초과가 나지 않으실 겁니다.
# 제 설명이 도움이 되면 좋겠습니다. 화이팅


# def solution(n,l,r): 
#     return [ ma\x(divmod(i,n))+1 for i in range(l,r+1)]

def solution(n, left, right):
    answer = []
    x = (right - left) +1
    for i in range(x):
        r = ((i+left) // n) + 1 # 행
        c = ((i+left) % n) + 1  # 열
        answer.append(max(r,c))
    return answer
print(solution(3,2,5)) #[3,2,2,3]

# https://hyojun.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-n2-%EB%B0%B0%EC%97%B4-%EC%9E%90%EB%A5%B4%EA%B8%B0-Java

# 다른살람 풀이 Divmod 이용
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        q, r = divmod(i, n) # 몫, 나머지

        answer.append(max(q, r) + 1)
    return answer
print(solution(3,2,5)) #[3,2,2,3]