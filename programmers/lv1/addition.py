# 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3

#행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
def solution(arr1, arr2):
    answer = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
# return [[4,6],[7,9]]