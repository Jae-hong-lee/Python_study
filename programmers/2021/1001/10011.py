#주식가격
#1,2,3,2,3 이 가격으로 주이고 초마다 변하는 값을 count 하는 느낌임.
#즉 1은 1 => 2,3,2,3 / 2는 2 => 3,2,3 / 3은 3 => 2,3 / 4은 2=> 3 / 5는  3 다음값이 없.
#1은 가격이 떨어질 일이 없고, 2도 마찬가지. = 그렇다면 남은 배열 카운트 숫자 출력 즉, 4,3
#3은 바로 다음 수가 2니까 1초만에 떨어지는거 , 1 출력
#4은 가격이 2 -> 3 으로 변하니까 가격이 떨어지지 않지만 남은 변수가 하나뿐이니, 1출력
#5은 떨어지지않음 다음수가 없으니까,  0출력.

#그냥 배열 만들어서 .pop 해서 하나씩 뺴고 지우고 남은 카운트 세면 될듯
#근데 pop 한 수가 다음 pop 한 값보다 작으면 안되네.
# def solution(prices):
#     answer = []
#     while prices:
#         x = prices.pop(0)
#         cnt = 0 #초기화값
#         if x <= prices[0]:
#             cnt +=1
#         else:
#             cnt+=1
#             break
#         #answer.append(cnt)
#         answer.append(len(prices))
#     return answer
# print(solution([1, 2, 3, 2, 3]))

# def solution(prices):
#     answer = []
#     while prices:
#         cnt = 0
#         x = prices.pop(0)
#         while prices:
#             cnt +=1
#             if x > prices[0]:
#                 break
#         answer.append(cnt)
#     return answer
# print(solution([1, 2, 3, 2, 3]))
#효율성 0점. 66.7점
#위의 두 코드는 모두 O( N2 )인 것은 맞긴 합니다.
#다만, 위의 코드는 최선의 경우가 나오면 O(N) 선에서 끝날 여지라도 있으나, 
#(가격이 떨어지기만 한다면 바로 옆의 가격만 확인하고 넘어가겠죠)
#pop(0) 동작을 리스트의 크기만큼 수행하는 코드는 최선의 경우가 나와도 O( N2 )이 됩니다.
#따라서 리스트를 모두 pop(0) 하는 동작만 하더라도 효율성 테스트에서 시간 초과가 되므로,
# 리스트의 pop(0)을 쓰지 않고 풀어야 합니다.
#굳이 맨 왼쪽부터 pop을 해야한다면, deque를 쓰는 방법도 있긴 합니다만, 
# 이런 식의 pop은 출제 의도가 아니긴 합니다.

#from collections import deque
#그렇다고한다....
from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer



# 이중 for문 ,효율성이 떨어질듯(?) ↑ 아님.
def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        count = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                count +=1
            else:
                count +=1
                break
        answer.append(count)
    
    return answer

print(solution([1, 2, 3, 2, 3]))


#stack
def solution(prices):
    answer = [0]*len(prices)
    stack = []
 
    for i, price in enumerate(prices):
        #stack이 비었이면 false
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
 
    # for문 다 돌고 Stack에 남아있는 값들 pop
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
 
    return answer
