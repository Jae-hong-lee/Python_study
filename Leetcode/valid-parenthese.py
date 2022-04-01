# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# { { { } [ ] [ [ ] ] ] }이(가) 유효한 표현식임
# stack 문제. 백준에서 푼거랑 비슷.
# s 문자열로 들어가져 있다.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        list_s = list(s)

        for i in list_s:
            if i== '[' or i=='{' or i=='(':
                stack.append(i)
            elif len(stack) != 0:
                if i ==')' and stack[-1] == '(' or i ==']' and stack[-1] == '[' or i =='}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        if len(stack) ==0:
            return True
        else:
            return False

    print(isValid(1,"()")) # true
    print(isValid(2,"()[]{}")) # true
    print(isValid(3,"(]")) # false



# stack 이 비어있지 않을때, 반복문 돌다가 stack 비워지고 닫힌 괄호일때????
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         list_s = list(s)

#         for i in list_s:
#             if i== '[' or i== '{' or i== '(':
#                 stack.append(i)
#             else:
#                 return False
        
#         if len(stack) !=0:
#             return False
            
        # return True


    # print(isValid(1,"()")) # true
    # print(isValid(2,"()[]{}")) # true
    # print(isValid(3,"(]")) # false


# (] 이부분 오류
# "({{{{}}}))"
# pop오류. 괄호 갯수는 똑같고 괄호가 다를때.
# stack 맨뒷부분과 동일할때로 바꿔야 할듯
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         list_s = list(s)

#         for i in list_s:
#             if i== '[' or i== '{' or i== '(':
#                 stack.append(i)
#             elif i ==')' and '(' not in stack or i ==']' and '[' not in stack  or i =='}' and '{' not in stack:
#                # stack.pop()
#                 return False
#             elif i ==']' or i ==')' or i =='}':
#                 stack.pop()
        
#         if len(stack) ==0:
#             return True
#         else:
#             return False
    # print(isValid(1,"()")) # true
    # print(isValid(2,"()[]{}")) # true
    # print(isValid(3,"(]")) # false
    # print(isValid(1,"({{{{}}}))")) # false



# index에서 벗어나짐. 마지막 FOR 끝날때가 문제인가?
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         list_s = list(s)

#         for i in list_s:
#             if i== '[' or i== '{' or i== '(':
#                 stack.append(i)
#             elif i ==')' and stack[-1] == '(' or i ==']' and stack[-1] == '[' or i =='}' and stack[-1] == '{':
#                 # return False
#                 stack.pop()
#             # elif i ==']' or i ==')' or i =='}':
#             #     stack.pop()
#             else: return False

#         if len(stack) ==0:
#             return True
#         else:
#             return False

#     print(isValid(1,"({{{{}}}))")) # false
