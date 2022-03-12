#최댓값과 최솟값
#문자열 s에는 공백으로 구분된 숫자들이 저장
#"(최소값) (최대값)"형태의 문자열로 반환

#예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, 
# "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

#1
# def solution(s):
#     answer = ''
#     #str에 나타나는 숫자중...이라는 것을 그냥 넘긴듯
#     n_min = min(n)#최소값
#     n_max = max(n)#최대값
#     answer = (n_min+" ".join+n_max) #타입에러..응애
#     return answer

def solution(s):
    answer = ''
    n = list(map(int,s.split(' '))) 
    #공백제거 ,str 값이니까 map 함수로 int 로 변환하고 list 로 n에담음
    n_min = min(n)#최솟값구하고
    n_max = max(n)#최대값 구하고
    answer = (str(n_min)+' '+str(n_max)) #문제를 읽어보면 둘 이상의 정수가 공백으로 구분.

    return answer
print(solution('1 2 3 4'))
