# def solution(s):
#     num_s = 'one two three four five six seven eight nine'
#     num= [1,2,3,4,5,6,7,8,9]
    
#     numbers=dict(zip(num,num_s.split()))
#     print(numbers)
#     answer = 0
    

#     s.sort()
#     print(s)
#     return answer
# print(solution("one4seveneight"))

#단어를 숫자로 변환하는 법을 구글링했음..도저히 변환법을 모르겠음
#질문하기도 한번 봣음
#결과 : 배열을 새로 만들어서 변환 -> 겹치는 부분은 어케 구분하나

#https://opentutorials.org/course/3094/17533
#딕셔너리 형태로 zip으로 풀 수 있을까?

# def solution(s):
#     answer = 0
#     a = ['zero', 'one', 'two', 'three', 'four',
#          'five', 'six', 'seven', 'eight', 'nine']
#     for i in a: #i는 a번째까지 반복...
#         s = s.replace(i, str(a.index(i))) 
#         #index로 a 배열에 i번째 인 단어를 찾고 스트링형으로 변환되어
#         #replace로 i번째 문자를 앞에 찾은 a배열의 단어로 바꾼다.

#     return int(s) #그러고 결과값은 정수형으로.
# print(solution("one4seveneight"))
# #replace란?? 문자열을 변경하는 함수
# #왜 replace를 생각을 못했을까.


# def solution(s):
#     num_s = 'zero one two three four five six seven eight nine'
#     num= [0,1,2,3,4,5,6,7,8,9]
#     numbers=dict(zip(num,num_s.split()))
#     #numbers= {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
#     print(numbers)
#     for k in numbers.items():
#         s = s.replace(k, str(numbers[1]))

#     return int(s)
# print(solution("one4seveneight"))
#문자열 길이로 변환해서도 풀 수 있을거 같다
#https://yjyoon-dev.github.io/kakao/2021/07/12/kakao-numstrengword/
#아까 확인한 isdigit과 isalpha로 푼 방법
#https://pearlluck.tistory.com/590