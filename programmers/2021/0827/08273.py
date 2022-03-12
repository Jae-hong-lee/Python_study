#최솟값 만들기
# A에서 첫번째 숫자인 1, B에서 
# 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
# A에서 두번째 숫자인 4,
#  B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
# A에서 세번째 숫자인 2,
#  B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)

#큰수랑 작은수 곱하고 더해줘야함.

#zip 이용, reverse 오름차순 내림차순.(k번째수는?)
#1
# def solution(A,B):
#     answer = 0

#     for i in range(len(A)):
#         answer += A[i] * B[i]

   
#     return answer
# print(solution([1, 4, 2],[5, 4, 4]))

#문제에서 보이는 식은 일단 만들어봄
#2 zip
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for a,b in zip(A,B):
        answer += a*b

   
    return answer
print(solution([1, 4, 2],[5, 4, 4]))
#zip 만 써서최솟값을 만들수가없음 그래서 오름차순과 내림차순 추가.