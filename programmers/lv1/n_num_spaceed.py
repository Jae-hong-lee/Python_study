# x만큼 간격이 있는 n개의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3



def solution(x, n):
    answer = []
    
    for i in range(1,n+1):
        answer.append(x*i)
    return answer

#그냥 쉽게 1부터 n까지 돌려서 i 값 만큼 x 곱해서 대입해주면됨
#처음에 제곱해야하나 했는데 아님.