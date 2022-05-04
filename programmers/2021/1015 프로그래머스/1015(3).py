#소수찾기
#한자리 숫자가 적힌 종이 조각이 흩어져 있음
#흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 한다.

#각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주여졌을 때,
#종이 조각으로 만들 수 있는 소수가 몇 개인지 return

#제한사항
#numbers는 길이 1 이상 7 이하인 문자열입니다.
#numbers는 0~9까지 숫자만으로 이루어져 있습니다.
#"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

# 11과 011은 같은 숫자로 취급합니다.
#소수 = 에라토스테네스의 체 , math 함수.

import math
def decimal(n):
    if n <=1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i ==0:
                return False
    return True
    #소수찾는 함수
    #소수는 2부터 이므로, x가 1보다 작거나 같으면 false
    #2부터 n의 제곱근까지 수 중 나누어지는 수가 있으면
    #(소수가 아니면) False
    #2부터 n의 제곱근까지 나누어지는 수 없으면 True(소수)
# def solution(numbers):
#     answer = 0
#     for i in range(len(numbers)+1):
#         for j in range(len(numbers)):
#             answer #어떻게 값을 만들어야할까.. 완전탐색..구글링
#완전탐색 = 모든 경우의 수.. (순열, 재귀함수)
#     return answer

# def solution(numbers):
#     result = [numbers[:]]
#     answer = 0
#     a = [0]*len(numbers)
#     while answer <len(numbers):
#         if a[answer]<answer:
#             if answer %2 ==0:
#                 numbers[0],numbers[answer] = numbers[answer],numbers[0]
#             else:
#                 numbers[a[answer]],numbers[answer] = numbers[answer],numbers[a[answer]]
#             result.append(numbers[:])
#             a[answer]+=1
#             answer = 0
#         else:
#             a[answer] = 0
#             answer+=1
    
#     return result
# print(solution("17"))
#순혈코드를 그대로 가져와봄..

from itertools import permutations
def solution(numbers):
    answer = []
    for i in range (1, len(numbers)+1):
        arr = list(permutations(numbers,i))
        #print(arr) 순열을 사용해 i개씩 묶어지는 list 생성
        for j in range(len(arr)): #생성된 list 길이만큼만 실행
            
            
            num = int(''.join(map(str,arr[j])))
            #list(arr) rkqtemfdms 튜플들로 이루어져 있으니 join,map함수 이용해서 join시키기
            if decimal(num): #소수일 경우 num 추가
                answer.append(num)
                
    answer = list(set(answer)) #set = 중복값 제거  (11,011은 같은 숫자취급)

    return len(answer)

print(solution("17"))
print(solution("011"))
#
#permutations(반복 가능한 객체, n)
#중복을 허용하지 않는다.
#순서에 의미가 있다 (= 같은 값이 뽑히더라도 순서가 다르면 다른 경우의 수로 판단)
# from itertools import permutations
# print(list(permutations([1,2,3,4], 2)))
# print(list(permutations([1,2,3,1], 2))) #2개의 원소로 수열 만들기

#https://www.youtube.com/watch?v=m3kCKV8oc1g
#정리..