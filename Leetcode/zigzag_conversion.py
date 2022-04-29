# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/

# 문자열 「PAYPALISHIRING」은, 다음과 같이 소정의 행수에 지그재그 패턴으로 기술되어 있습니다.(이 패턴을 보다 읽기 쉽게 하기 위해서 고정 폰트로 표시할 수도 있습니다)
# 그다음에 "PAHNAPLSIIGYIR"한 줄씩 읽어드릴게요.
# 문자열을 사용하는 코드를 입력하고, 다음과 같이 여러 개의 행을 지정하여 변환합니다.

# 위에서 아래로 한글자씩 저장. 높이의 길이는 numRows로 지정해줌.
# -> numRows 의 수 만큼 박스를 만드는 것. 그리고 그 박스에 한글한글자 담는거 그 다음 합치기
# 그다음 옆으로 한줄씩 읽어서 붙여서 return 한 문자열이 정답

# 파이썬 빈 목록만들기
# 1  값 넣다보니 깨달음 -> 3개 3개 3개 이런식이 아닌 3개 1개 3개 이런식.
#   numRows-2해줘야한다.
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if len(s)==0: return 0
#         # stack = [[] * i for i in [numRows]] # 배열에 값이 있어야 여러개 나옴, 2차원 배열 말고 1차원 배열로 ['','',''] 만들고 싶음
#         # stack = [[''] * i for i in [numRows]] 
#         stack = [''] * numRows;
#         # print(stack)
#         count = 0
#         for word in s:
#             stack[count]+=word
#             count+=1
# l = Solution()
# print(l.convert("PAYPALISHIRING",3)) # "PAHNAPLSIIGYIR"
# print(l.convert("PAYPALISHIRING",4)) # "PINALSIGYAHRPI"

#2
# 화살표 흐름대로 인덱스를 조작해서 stack 에 넣어서 출력 
# 인덱스 조작을 어케할까? ->  함수를 만들어서 0일땐 up 으로 들어가서 3까지 의 수 스택에 쌓는 함수
# 아니라면 down 들어가서 0까지 스택에 쌓기
# 이렇게하면 중간에 껴있는 저 하나는 안들어감.
# 나누기 이용?? - 
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if len(s)==0: return 0
#         stack = [''] * numRows;
#         # print(stack)  
#         count = 0
#         # while len(s):
#         #     count+=1
#         for word in s:
#             # count = count  /numRows 
#             count = count % numRows
#             # if count == 0:
#                 # down(count,numRows,s)
#             # elif count ==5:
#                 # up(count,numRows,s)
#     # 나누기 이용하자
# 333
# l = Solution()
# print(l.convert("PAYPALISHIRING",3)) # "PAHNAPLSIIGYIR"
# print(l.convert("PAYPALISHIRING",4)) # "PINALSIGYAHRPI"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)==0: return 0
        if numRows == 1:
            return s
        stack = [''] * numRows;
        index = 0
        count = 1
        for i in range(len(s)-1):
            stack[index] += s[i]
            index += count
            if index == numRows-1 or index==0:
                count *=-1
            
        # print(''.join(stack))
        return ''.join(stack)
                
l = Solution()
print(l.convert("AB",1)) # "PAHNAPLSIIGYIR"
print(l.convert("PAYPALISHIRING",3)) # "PAHNAPLSIIGYIR"
print(l.convert("PAYPALISHIRING",4)) # "PINALSIGYAHRPI"

# https://redquark.org/leetcode/0006-zigzag-conversion/