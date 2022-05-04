#H-Index
# 과학자가 발표한 논문 n편 중,h번 이상 인용된 논문이 h편 이상이고
# 나머지 논문이 h번 이하 인용되었다면
# h의 최댓값이 이 과학자의 H-Index returns

#과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
#논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

# 어떤 과학자가 발표한 논문 n편 중, 
# h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 
# 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
# 배열 개수중 가운데 값이 h값이 되고 그 h값을 통해서 h-index 를 구해서 return 값을 구한다


#문제이해
# 예를들어 [4, 4, 4, 4,// 5, 5, 5, 5, 5, //6, 6, 6, 6, 6, 6] 이라는 리스트가 있을때,

# 우선 “h번 이상 인용된 논문이 h편 이상” 에 부합하는 경우를 찾아보면

# 4회 이상 인용된 논문이 4개 이상 (15개),
# 5회 이상 인용된 논문이 5개 이상 (11개),
# 6회 이상 인용된 논문이 6개 이상이다 (6개).
# 이렇게만 보면 H-INDEX가 세 개나 나온 것 같지만, 그렇지않다.

# “나머지 논문이 h번 이하 인용되었다면” 이라는 조건까지 따져보면,

# 4회 이상 인용된 논문이 4개 이상, 하지만 나머지 논문 중에 4번 초과 인용된 논문이 존재함. (5, 6)
# 5회 이상 인용된 논문이 5개 이상, 하지만 나머지 논문 중에 5번 초과 인용된 논문이 존재함. (6)
# 6회 이상 인용된 논문이 6개 이상, 또한 나머지 논문은 전부 6회 이하 인용 (4, 5)
# 따라서 문제의 조건에 완벽히 부합하는 H-INDEX는 6 하나밖에 없다는 사실을 알 수 있다.

# 다시 말해, “h번 이상 인용된 논문이 h편 이상이되는, h의 최대값”을 구하는 것과 같다.
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)+1):
        h = sum(j>=i for j in citations)
        k = sum(j<=i for j in citations)
        if h>= i and k <=i:
            if i>answer : answer =i
    if citations[0] >= len(citations): answer = len(citations)

    return answer
print(solution([3, 0, 6, 1, 5]))


# def solution(citations):
#     answer = 0
#     citations.sort()
#     for i in range(len(citations)):
#         for j in citations:
#             if citations[i]<= citations[j]:
#                 answer +=1
    

#     return answer
# print(solution([3, 0, 6, 1, 5]))

# 주어진 배열에서 특정 수 A가 나왔을 때 그 숫자와 같거나 큰 숫자들의 갯수를 센다.
# A와 같거나 큰 숫자들이 A갯수 이상일 때 A에 대한 h-index 후보는 A가 된다.
# 만약 주어진 배열에서 A와 같거나 큰 숫자들 A갯수 미만일 때는 A는 후보에 들지 못한다.
# 난 코드에서 이 숫자를 quote(인용)라는 이름의 list로 정의했다.
 
# 예제로 주어진 3, 0, 6, 1, 5에 대해서 이를 정의해보자.
# 3번 이상 인용된 논문은 3, 6, 5 총 3개이므로 3번 인용된 논문에 대한 h-index 후보는 3이 된다.
# 마찬가지로 0번 이상은 5개이므로 h-index 후보는 0
# 6번 이상은 1개이므로 0
# 1번 이상은 4개이므로 1
# 5번 이상은 2개이므로 0
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) -i:
            answer =len(citations)-i
            break
    return answer
print(solution([3, 0, 6, 1, 5]))
#오름차순 정렬 후 증가하는 인덱스 루프에서 현재 값이 남은 개수보다 크거나 같을 때의 남은 개수.
#현재값이 뒤에 있는 원수 갯수보다 클 경우 h번 이상 인용된 논문이 h편 이상 조건을 만족