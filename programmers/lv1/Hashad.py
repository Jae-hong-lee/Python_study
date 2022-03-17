# 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
def solution(x):
    y = str(x)
    sum = 0 
    
    for i in range(len(y)):
        sum += int(y[i])
        if x % sum ==0:
            answer = True
        else :
            answer =  False
    
    return answer
print(solution(10))