# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# 문자열 s를 지정하면 의 가장 긴 회문 서브스트링을 반환합니다.
# Explanation: "aba" is also a valid answer. #  유사한 답변이다?;

# 펠린드롬 넘버. 
# reverse한 결과와 원본이 같은 단어 +++ 가장 긴 palindromic substring
# 가장긴거 뽑아내기.
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         y = str(x)[::-1]
#         # print(y)
#         if str(x) == y:
#             return True
#         else:
#             return False

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s # 문자열이 하나 주어졌을때.

        
    print(longestPalindrome(1,"babad"))
    print(longestPalindrome(2,"cbbd"))
