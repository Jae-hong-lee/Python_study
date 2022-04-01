# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

# 문자 다 비교 -> 완전탐샊??
# 가장짧은걸 기준으로 비교해야할듯?

# 배열 문자열길이별로 정렬하기 
# https://pybasall.tistory.com/67
# class Solution:
#     def longestCommonPrefix(self, strs: str) -> str:
#         if len(strs) == 0: return ""
#         strs.sort(key=len)
        # print(strs)
        # print(strs[0])
#         # for i in range(len(strs)):
#         #     a = strs[i]
        
#     print(longestCommonPrefix(1,["flower","flow","flight"]))
#     print(longestCommonPrefix(2,["dog","racecar","car"]))


# 가장 짧은 글자를 기준으로 정한다.
# 가장짧은 글자 길이만큼 FOR 문돌려서 다른 문자들이랑 비교?
# class Solution:
#     def longestCommonPrefix(self, strs: str) -> str:
#         if len(strs) == 0: return ""
#         strs.sort(key=len)
#         Criteria = strs[0]
#         # 기준 단어 지정 indexof 함수 없나..
#         # find? 활용? index?
#         answer = ""
#         for i in range(1,len(strs)):
#             for j in range(len(Criteria)):
#                 if strs[i][j] == Criteria[j]:
#                     answer += Criteria[j]
#                 else:
#                     return answer

# flowfl 이 나와버림 초기화를 어케 시키냐  
# 두번째 단어지나고 세번째 단어랑 비교할때 같이 그대로 들어있음              
    # print(longestCommonPrefix(1,["flower","flow","flight"]))
    # print(longestCommonPrefix(2,["dog","racecar","car"])) # ""


# class Solution:
#     def longestCommonPrefix(self, strs: str) -> str:
#         if len(strs) == 0: return ""
#         strs.sort(key=len)
#         Criteria = strs[0]

#         answer = ""
#         for i in range(1,len(strs)):
#             temp = Criteria[i]
#             for j in range(len(Criteria)):
#                 if strs[i][j] == Criteria[j]:
#                     answer += Criteria[j]
#                 else:
#                     return answer
#     print(longestCommonPrefix(1,["flower","flow","flight"]))
#     print(longestCommonPrefix(2,["dog","racecar","car"])) 

class Solution:
    def longestCommonPrefix(self, strs: str) -> str:
        if len(strs) == 1: 
            return strs[0]
        strs.sort(key=len)
        Criteria = strs[0]
        answer = ""
        for i , string in enumerate(Criteria):
            for s in strs:
                if s[i] != string:
                    # answer =  Criteria[:i]
                    return Criteria[:i]
                    # return answer
                # if s[i] == string:
                #     if answer(s[i]).count <3:
                #         answer += s[i]
            
        # return answer
        return Criteria
        
    # ffflll 으으응으음 중복값이 3개이상일때 answer c출력?
    # a 일때 "" 이 출력이 안댐?;
    # 조건이 맞지 않을때 기준값(Criteria) 출력으로 바꿈 ㅇㅋ~
    print(longestCommonPrefix(1,["flower","flow","flight"]))
    print(longestCommonPrefix(2,["dog","racecar","car"])) 
    print(longestCommonPrefix(3,["a"])) 