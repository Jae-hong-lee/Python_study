# 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945
#  def solution(n):
    
#     if n <2:
#         return n
#     else:
#         return solution(n-1)+solution(n-2)
    
# print(solution(5)) 효율성 측면에서 안나옴. for문 이용해야할듯 42.9점

def solution(n):
    answer = 0
    x, y = 0,1
    if n <2:
        return n #n이 2이하면 더해지지 않으니 0,1 n을 출력 1번째 2번째 수.
    else:

        for i in range(n):
            x,y = y, x+y
        return x
    # for i in range(n):
    #     solution(n-1), solution(n-2) = solution(n-2), solution(n-1)+ solution(n-2)
    # return solution(n-1)
print(solution(5))
#런타임에러 42.9점 똑같음 위에 풀이랑
#https://psychoria.tistory.com/770 피보나치 참고
#2 이상이 n이 입력되었을 때, n번째 피보나치 수를 1234567로 나눈 나머지 함수를 리턴 하라,,,
#재귀함수로도 풀 수 있음 if == 0 , if==1

def solution(n):
    x=0
    y=1
    if n <2:
        return n
    else:
        for i in range(n):
            answer = x+y
            x= y
            y = answer
        return x%1234567