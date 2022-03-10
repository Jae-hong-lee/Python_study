# 1. 카펫
# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고
# 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

# Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만,
# 전체 카펫의 크기는 기억 X

# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로
# 주어질 떄 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 함수작성

# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

# 사각형 격자의 수..를 주목했다.. 격자의 수를 구하는법??
# https://snowall.tistory.com/1891 식이 존나많네
# (yellow의 가로 길이 +2 ) + (yellow의 세로길이 +2) *2 -4 (*겹치는 사각형 제외)
# 겹치는 사각형이란? - 꼭짓점? = 4개의 꼭짓점.(사각형)
# = brown 갯수..?
# 공식 수정 : (yellow 가로길이 + yellow 세로길이) * 2 + 4 = brown 갯수
# ?? 그냥 yellow 가로 세로 길이에 +2 하면 brown 가로 세로가 나오네..

# 규칙은 알아냈는데 yellow 의 가로 세로 값은 어케 구하지..?
# 가로세로 규칙만 알아내면 알아낸 브라운 갯수로 똑같이 적용하면 풀릴거 같은데
# 그 규칙을 모르겠음.

def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):
        if yellow*2 + i*2 +4 ==brown:
            return[yellow+2,i+2]
        
    return answer
print(solution(10,2)) #[4,3]
print(solution(8,1)) #[3,3]
print(solution(24,24)) #[8,6]
# 1,2번 예제는 통과함..
# 24,24 와 36,64 같은 수들은 어뜨케 처리하느냐..


def solution(brown, yellow):
    x = yellow
    for y in range(1, yellow+1):
        if x*2 + y*2 + 4 == brown:
            return [x+2, y+2]
        x = yellow // (y+1)
print(solution(10,2)) #[4,3]
print(solution(8,1)) #[3,3]
print(solution(24,24)) #[8,6]
# 61.5점

#다른사람 풀이
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for x in range(1,total +1):
        if (total / x) %1 ==0:
            a = total /x
            if a>=x:
                if 2*a + 2*x == brown +4:
                    return[a,x]
    return answer

print(solution(10,2)) #[4,3]
print(solution(8,1)) #[3,3]
print(solution(24,24)) #[8,6]