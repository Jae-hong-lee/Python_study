# 2. 큰 수 만들기
# 탐욕법(Greedy)
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 한다.
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 
# 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 
# solution 함수의 매개변수로 주어집니다.
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 
# 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 제한조건
# number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.

# def solution(number, k):
#     answer = ''
#     x =[]
#     arr = []
#     for num in number:
#         x.append((num))

#     for i in range(len(x)):
#         for j in range(i+1, len(x)):
#             if not i ==j:
#                 arr.append(x[i]+x[j])
#     int_arr = list(map(int,arr))
#     answer = str(max(int_arr))

#     return answer

#첫번째 시도 : 자릿수 생각을 안함 k...?
#문제 이해부족.
#앞에 있는 숫자를 우선순위로 수를 만들고, 만들어진 숫자중 가장 큰수를 찾아서 뽑아냄.(X)
#그냥 앞뒷 자리 비교해서 작으면 빼는걸 K만큼 반복시키면됨.. 2,3번째 문제 예를 보니..

# def solution(number, k):
#     answer = ''
#     x =[]
    
#     for num in number:
#         x.append(int(num))
#     for i in range(k):
#         cnt = 0
#         for j in range(len(x)):
#             if str(x[:j]+x[j+1:]) > cnt:
#                 cnt = x[:j] + x [j+1:]
#         x=  str(cnt)
#     answer =x
#     return answer

# print(solution("1924",2)) # "94"
# print(solution("1231234",3)) # "3234"
# print(solution("4177252841",4)) # 775841
# 타입에러..


# def solution(number, k):
#     answer = ''
#     for i in range(k):
#         cnt = 0
#         for j in range(len(number)):
#             if int(number[:j]+number[j+1:]) > cnt:
#                 cnt = int(number[:j] + number[j+1:])
#         number=  str(cnt)
#     answer = number
#     return answer

# print(solution("1924",2)) # "94"

#58점 시간초과....
#10의 자리에 들어갈 수 있는 수 중 가장 큰 수를 찾아서 일이 자리에 들어가는 수 중
#가장 큰 수를 찾는방법...
#[1,9,2] 중 가장 큰 수 9 [2,4]에서 가장 큰 수 4를 찾아서.. 94를 만들어봄


#그리디 + 스택 문제라고한다
def solution(number, k):
    answer = ''
    q = []
    popcnt = 0
    for num in number:
        while q and q[-1] < num:
            if popcnt == k:
                break
            q.pop()
            popcnt += 1
        q.append(num)
    answer = ''.join(q[:len(q) - k + popcnt])
    return answer
print(solution("1924",2)) # "94"
print(solution("1231234",3)) # "3234"
print(solution("4177252841",4)) # 775841
#앞자리에서부터 세어나가며 내림차순이 되도록 만듬..
#숫자를 스택에 하나씩 쌓아 올려가되 내림차순으로.
#즉, 스택을 쌓다가 스택 가장 윗자리 숫자보다 큰 숫자가 나오먄
#스택을 내림차순이 될 때 까지 pop한다

#k개를 pop 해주었으면 나머지 숫자는 그대로 내비둠.

#pop한 갯수가 k보다 부족하면 부족한 수 만큼 뒤에서 덜어줌
# (내림차순이므로 뒤에 숫자를 빼는게 유리.)