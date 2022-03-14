# https://leetcode.com/problems/roman-to-integer/
# 13. Roman to Integer
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# IV. 1은 5보다 앞에 있기 때문에 빼서 4가 됩니다. 
# 로 쓰여진 숫자 9에도 동일한 원칙이 적용됩니다 IX. 
# 빼기가 사용되는 6가지 경우가 있습니다.

# 딕셔너리 값을 만들고 값을 answer 에 다 넣고 더해서 출력
# 값이 작은건 뒷숫자에서 앞숫자 빼고 추가

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = list(str(s))
        answer = 0
        arr = []
        for i in s:
            x = dic.get(i)
            arr.append(dic.get(i))
            if answer < x:
                arr.append(-answer)
                arr.append(-answer)
            answer = x 
        print(sum(arr)) #int

            
l = Solution()
print(l.romanToInt("MCMXCIV")) #1994
# print(l.romanToInt('III'))
# print(l.romanToInt("LVIII"))
# l = Solution()
# print(l.isPalindrome(-121))        
# 인덱스값 에러 존나뜨네. 그냥 answer 담고시작.

# for in 활용할걸?
# 그냥 replace 로 풀걸?

        # answer = [dic[s[len(s)-1]]]
        # for i in range(1,len(s)):
        #     if dic[s[i]]<= dic[s[i-1]]: # III 같을때도 생각.
        #         answer.append(dic[s[i-1]])
        #     else:
        #         answer.append(-dic[s[i-1]])
        # return sum(answer)




# 바보 같이 뒤에 문자 숫자가 작으면 빼서 더해준다만 생각해서 중복값이 찍힘.
        # for i in range(1,len(s)):
        #     # print(i)
        #     # print(dic[s[i]])
        #     # print(dic[s[i-1]])
        #     # print('----')
        #     if dic[s[i]] < dic[s[i-1]]:
        #         answer.append(dic[s[i-1]])
        #     else:
        #         answer.append(dic[s[i]]-dic[s[i-1]])
        # return answer
# [1000, 900, 1000, 90, 100, 4] 



# 첫번째.
        # for i in range(len(s)): #IndexError: string index out of range
        #     if dic[s[i]] < dic[s[i+1]]: # 인덱스에서 벗어나짐
        #         answer.append(dic[s[i]])
        #     else:
        #         answer.append(dic[s[i]])

        # return answer # 잘나오면 sum 구해서 합 구하기?

# 두번째 : 앞뒤 문자 작으면 빼기.
        # for i in range(1,len(s)):
        #     # print(i)
        #     print(dic[s[i]])
        #     print(dic[s[i-1]])
        #     print('----')
        #     if dic[s[i]] < dic[s[i-1]]:
        #         answer.append(dic[s[i-1]])
        #     else:
        #         answer.append(dic[s[i-1]])
        # return answer