# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

# 정수가 주어지면 회문 정수인 경우 x를 반환 합니다.true x
# 정수는 정방향과 역방향이 같을 때 회문 입니다.
# 예를 들어 121는 회문이고 123는 그렇지 않습니다.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]
        print(y)
        if str(x) == y:
            return True
        else:
            return False
            
l = Solution()
print(l.isPalindrome(-121))

# x 가 int 형으로 들어가 값을 비교할때 에러뜸 -121일때 y = 121- 
# class Solution: 
    # def isPalindrome(self, x: int) -> bool:
    #     y = str(x)[::-1]
    #     # print(y)
    #     if x == y:
    #         return True
    #     else:
    #         return False