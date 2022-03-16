# 없는 숫자 더하기
# https://programmers.co.kr/learn/courses/30/lessons/86051

# 입출력 예 #1
# 5, 9가 numbers에 없으므로, 5 + 9 = 14를 return 해야 합니다.
# 입출력 예 #2
# 1, 2, 3이 numbers에 없으므로, 1 + 2 + 3 = 6을 return 해야 합니다.
def solution(numbers):
    answer =0
    c = [0,1,2,3,4,5,6,7,8,9]
    numbers.sort()
    sum = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer
print(solution([1,2,3,4,6,7,8,0])) #result 14