#올바른괄호
#괄호가 바르게 짝지어졌다는 것 '(' 로 열렸다. ')' 로 닫혀야함
# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
#문자열s 가 주어졌을 떄, 문자열 s가 올바른 괄호면 True,
#  올바르지 않으면 false 를 return

# def solution(s):
#     answer = True
#     a=[]
#     for i in range(len(s)):
#         if s[i] =='(':
#             a.append(s[i])
#         else:
#             pop()
#
#
#     if len(a) > 0:
#         return False
#     else:
#         return True
# a배열에 들어있는 ( 을 비교하는 ?? 조건문이 없음..


# def solution(s):
#     answer = True
#     arr = []
#     for i in range(len(s)):
#         if s[i] == '(':
#             arr.append(s[i])
#         else:
#             if arr[:-1] == '(':
#                 arr.pop()
#             else:
#                 arr.append(s[i])
#     if len(arr)>0:
#         return False
#     else:
#         return True
#    # return True
# print(solution("()()"))
# print(solution("(())()"	))
# print(solution(")()("))
#새로운 배열을 만들어서 s길이만큼 for문을 통해 돌리고
#'(' 로 시작하면 arr배열에 넣고 ')'로 시작하면 pop해서 빼주고
#arr가 남아있다면 false 없다면 True 출력하기
#문제점. 두번 if문 arr[] 몇번째..

# def solution(s):
#     answer = True
#     arr = []
#     for i in range (len(s)):
#         if s[i] == '(':
#             arr.append(s[i])
#         else:
#             if arr[0] == '(':
#                 arr.pop()
#             else:
#                 arr.append(s[i])
#     if len(arr) > 0:
#         return False
#     else:
#         return True 
# print(solution(")()(" ))          
#IndexError: list index out of range 
#3번쨰 경우의 수에서 ) 부터 들어가지니 값이 없으니 팝이 불가함..

# def solution(s):
#     answer = True
#     arr = []
#     for i in range (len(s)):
#         if s[i] == '(':
#             arr.append(s[i])
#         else:
#             if arr : 
#                 if arr[0] == '(':
#                     arr.pop()
#                 else:
#                     arr.append(s[i])
#     if len(arr) > 0:
#         return False
#     else:
#         return True

# print(solution(")()(" ))  
#if arr: 를 통해 ) 로 시작하면 다시 올라가서 for 문 실행
#73점. 정확성이 떨어짐.2~6,11,18

def solution(s):
    answer = True
    arr = []
    for i in range (len(s)):
        if s[i] == '(':
            arr.append(s[i])
        else:
            if len(arr) >0 and arr[0] == '(':
                arr.pop()
            else:
                arr.append(s[i])
                
    if len(arr) > 0:
        return False
    else:
        return True

print(solution(")()(" ))  
#if arr 를 그냥 and 로 바꿈. 