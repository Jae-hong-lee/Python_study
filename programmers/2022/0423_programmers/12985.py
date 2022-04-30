# 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

# 대회는 N명이 참가, 토너먼트형식, N명의 참가자는 각각 1부터 N번을 차례대로 배정
# 1번 - 2번, 3번 - 4번...참가자끼리 게임 진행
# 다음 라운드에 진출할 참가자의 번호는 다시 배정, 게임은 최종 한 명이 남을 때까지
# 만약 1번-2번 겨루는 게임에서 2번 승리시 다음라운드 1번    짝수시 1번
# 3번-4번 겨루는 게임에서 3번이 승리시 다음라운드 2번       홀수시 2번

# 단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.
# A랑 B가 만나게 되는 라운드 return, 부전승은 없다!!
# N : 2에1승 이상 2에20승 이하인 자연수 (2의 지수 승으로 주어지므로 부전승은 발생하지 않습니다.)

# 첫 번째 라운드에서 4번 참가자는 3번 참가자와 붙게 되고, 7번 참가자는 8번 참가자와 붙게 됩니다. 
# 항상 이긴다고 가정했으므로 4번 참가자는 다음 라운드에서 2번이 되고, 7번 참가자는 4번이 됩니다.
#  두 번째 라운드에서 2번은 1번과 붙게 되고, 4번은 3번과 붙게 됩니다. 
# 항상 이긴다고 가정했으므로 2번은 다음 라운드에서 1번이 되고, 4번은 2번이 됩니다. 
# 세 번째 라운드에서 1번과 2번으로 두 참가자가 붙게 되므로 3을 return 하면 됩니다.

# 짝수시 홀수로 홀수시 짝수로>?
# N /2 /2 /2 로 계속 나눠줘야함?? 재귀, while문 ??
# 짝수를 나누면 매치.
# def solution(n,a,b):
#     answer = 0
#     # 몫 : a// 2 = 2 , b//2 = 3 
#     # 나머지  a%2 = 0 , b% 2 = 1
#     while True: #8//2 -1 = 총라운드수.
#         answer+=1
#         a =  a//2 
#         b =  b//2
#     # ???????????????
#     return answer
print(solution(8,4,7)) #answer 3


# 홀수 일때는 나머지 1 을 + 해주고 a==b 라운드수가 같을 경우 종료
# 이 식을 돌렸을때 마지막 라운드 a=1,b=2가 나올때 오류뜸
# 홀수만 +1 해주면 될줄 알았는데 이렇게 하면 a가 홀수가 나오면 오류날듯
# 두개다 나누어떨어지는지 판별해주어야하고 1,2이렇게 나올때도 생각해야함.
# 한쪽만 나눠서 라운드를 맞춰주고 있었음 a,b 둘다 라운드를 계산해주자.
# def solution(n,a,b):
#     answer = 0
#     round = n//2 -1 #3 총 라운드수
#     while round>0:
#         if b%2: #==0
#             b+=1
#         a,b = a//2, b//2
#         answer += 1
#         round  -= 1
#     return answer
# print(solution(8,4,7)) #answer 3


# 틀림 round 을 잘못정한듯. while 문 쪽에서 문제난듯.
# def solution(n,a,b): 
#     answer = 0 
#     round = n//2 -1
#     while round >0: 
#         if a%2: 
#             a += 1 
#         if b%2:
#             b += 1 
#         a, b = a//2, b//2 
#         answer += 1 
#         round -= 1
#     return answer

# print(solution(8,4,7)) #answer 3



# a가 1일때가 부분에서 조금 헤멤...
def solution(n,a,b): 
    answer = 0 
    # round = n//2 -1
    while True: 
        if a%2: 
            a += 1 
        if b%2:
            b += 1 
        a, b = a//2, b//2 
        answer += 1 
        if a==b: 
            #같은 라운드니까 break로 무한루프 탈출
            break
    return answer

print(solution(8,4,8)) #answer 3


# 제출
def solution(n,a,b): 
    answer = 0 
    while a!=b:
        if a%2: 
            a += 1 
        if b%2:
            b += 1 
        a, b = a//2, b//2 
        answer += 1 
    return answer

print(solution(8,4,7)) #answer 3