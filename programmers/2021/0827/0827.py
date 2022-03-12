# 행렬의 곱셉
#  2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, 
# solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
# 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
# 곱할 수 있는 배열만 주어집니다.

# 수도 코드 
# def solution(arr1, arr2):
#     answer = [[]]
#     for i in range(len(arr1)):
#         for j in range(len(arr2)):
#             for k in range(len(arr2)):
#                 answer.append(arr1[i][k] * arr2[j][k])

#     return answer

# print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))

# i 는 arr1에 몇번쨰 행렬을 쓸껀지
# j 는 arr2에 몇번째 행렬을 쓸껀지
# k 는 0번쨰부터~ 라는뜻으로 씀
#이렇게 하면 arr1 은 i번째 행렬에 k번째 수를 뽑을 수 있음  =arr2
#그러고 answer 에 곱해서 넣으니까 더해져서 다 곱해졌다고 해야하나..?
#https://www.youtube.com/watch?v=JpSe38UHaos 행렬의 곱부터 공부해야할듯

def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):  
        line = [] #새로운 배열
        for j in range(len(arr2)): #arr2 의 개수만큼 돌리면 행렬의 곱 값이 달라짐.
            num=0
            for k in range(len(arr2)):
                num+=(arr1[i][k] * arr2[k][j])#연산결과(*)를 num 에 담음, 행렬의 곱
            line.append(num)#num값을 line 배열에 추가
        answer.append(line)#line 배열에 arr2 의 갯수만큼만 반복되어 저장되어 있는  수를 
        #answer 에 line 배열을 추가

    return answer

print(solution(	[[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))