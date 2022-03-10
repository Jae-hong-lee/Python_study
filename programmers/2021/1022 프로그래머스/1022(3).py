# 3.구명보트 탐욕법(Greedy)
# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려 한다.
# 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있다.

# 예를 들어, 사람들의 몸무게가 [70,50,80,50]이고 구명보트의 무게 제한이
# 100Kg 이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만
# 1번째 사람과 3번째 사람의 무게의 합은 150kg 이므로 
# 구명보트의 무게 제한을 초과하여 같이 탈 수 없다.

# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가
# 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return

# 제한사항
# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 
# 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

# # 트럭문제랑 비슷한 문제? 
# def solution(people, limit):
#     answer = 0
#     return answer

# print(solution([70, 50, 80, 50],100)) #3
# print(solution([70, 80, 50],100)) #3



# def solution(people, limit):
#     answer = 0
#     x = []
#     cnt = 0
#     while len(people) > cnt:        
#         for i in range(len(people)):
#             if people[0]+ people[i]<=limit:
#                 people.pop(0)
#                 cnt+=1
#                 answer +=1
#             else:
#                 cnt +=1
#                 answer +=1
#     return answer

# print(solution([70, 50, 80, 50],100)) #3
# print(solution([70, 80, 50],100)) #3
# 조건문에 값이 잘못되었다..
# while 조건도 잘못된듯 하다.
# 앞뒤 값을 더해서 Limit 값과 비교하면서 카운트를 세서 반복문에서 빠져나오도록
# 하려고 했는데 실패. 1차.

# def solution(people, limit):
#     answer = 0
#     x = []
#     cnt = 0
#     people.sort()
#     while len(people) >1:
#         if len(people) >1 and people[0] + people[-1] <= limit:
#             if len(people) ==2:
#                 people.pop(0)
#             else:
#                 for j in range(len(people)):
#                     if people[j] + people[-1] <= limit:
#                         people.pop(0+j)
#                         break
#         answer +=1
#         people.pop()            
#     return answer

# print(solution([70, 50, 80, 50],100)) #3
# print(solution([70, 80, 50],100)) #3

# 2차 실패.
# 배의 타는 사람은 최대 2명이라는 것, 정렬
# def solution(people, limit):
#     answer = 0
#     people.sort()
#     cnt =0
#     while len(people) > 0:
#         pp = people.pop()
#         x = limit - pp
#         if people[answer] <= x:
#             cnt +=1
#             people.pop()
#         else:
#             cnt+=1


#     answer = cnt
#     return answer

# print(solution([70, 50, 80, 50],100)) #3
# print(solution([70, 80, 50],100)) #3
# 두번째에서 실패.. 첫번째 예제는 통과.. people[0] <-이부분을 바꿔줘야할거같다.
# 사람들 몸무게를 정렬하고 앞에 있는 숫자를 pop해서 그 값을 limit 에 뺴서
# 그 값이 다음 값이랑 같거나 큰값이면 카운트 시키고 뺴고 다음사람.비교
# 그렇지 않다면 카운트 +1 하고 다음값 비교? 
# 이런식으로 풀어야할거같다. 물론위에도 그렇게 풀려고 했지만 잘 안댐.

# def solution(people, limit):
#     answer = 0
#     people.sort(reverse = True)
#     cnt =0
#     while len(people) > 0:
#         pp = people.pop()
#         x = limit - pp
#         if len(people) >0 and people[-1] <= x :
#             cnt +=1
#             people.pop()
#         else:
#             cnt+=1


#     answer = cnt
#     return answer

# print(solution([70, 50, 80, 50],100)) #3
# print(solution([70, 80, 50],100)) #3

#and 로 people에 값이 있을경우 라는 조건을 추가함
# 코드 실행은 통과함. 30점나옴 ㅅㅂ;

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    start = 0
    end = len(people)-1
    while start < end: #end 값은 for i in range(len(people)): 이라고 생각. 마지막값.
        if people[start]+people[end] <= limit:
            answer += 1
            start += 1
            end -= 1
        else:
            answer += 1
            start += 1
    answer += len(people[start:end+1]) #슬라이싱 끝낼 위치로 end는 포함이 안되기 떄문에 +1
    # print(start)
    # print(end)
    # print(people[start:end+1]) #len([3:3]) = 0 , len([2:3]) = 1
    return answer
print(solution([70, 50, 80, 50],100)) #3
print(solution([70, 80, 50],100)) #3
#풀이 1
#(정렬)첫과 끝값을 비교. 그후 start 값을 올려서 end값보다 커지면 반복문을 빠져나오는.

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
print(solution([70, 50, 80, 50],100)) #3
print(solution([70, 80, 50],100)) #3
# 풀이 2 이게 best 풀이 같다.
#짝 지었을때만 2명씩 나가니까 전체 인원에서 짝지은 수만 뺴주면 보트의 수가 나온다..