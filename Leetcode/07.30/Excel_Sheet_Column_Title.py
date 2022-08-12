# https://leetcode.com/problems/excel-sheet-column-title/
# 168. Excel Sheet Column Title
# 정수 열 번호에 해당하는 열 제목을 Excel 시트에 나타나는 대로 반환합니다.

# EX
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 

# 알파벳 배열 만들고, 26 나누기 
# columnNumber 가 26 이하라면 그대로 alpha[columnNumber]로 알파벳 출력

# 3. 26보다 크면 나머지 몫 규칙을 사용하고 나머지가 0이면 2가지 가능한 방법이 있습니다 .
#  몫 이 "1"이면 인덱스 [r-1](' r'은 나머지), 
# 그렇지 않으면 num =(q-1)에서 함수를 호출하고 문자 인덱싱 [r-1] 앞에 추가합니다.
# 4. 나머지가 "0"과 같지 않으면 num = (q)에 대한 함수를 호출하고 문자 인덱싱 [r-1] 앞에 추가합니다 .

#  몫은 quotient / 나머지는 remainder 

# IndexError: string index out of range
# answer += alpha[quotient-1]+alpha[remainder-1]
# 나누어 떨어질때를 생각했어야함.

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
      alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      answer = ""
      if columnNumber < 26:
        answer += alpha[columnNumber-1]
      else:
        quotient = columnNumber // 26 # 몫
        remainder = columnNumber % 26 # 나머지
        if remainder == 0:
          return 0

        print(quotient, remainder, self)
        # print (alpha[quotient-1], alpha[remainder-1], self)
        # return "27이상"


      return answer

    print(convertToTitle(1,1)) # A 1부터시작.
    print(convertToTitle(2,26)) # Z
    print(convertToTitle(2,28)) # AB
    print(convertToTitle(3,701)) # ZY



# Math 을 이용한 26진수를 통한 다른사람 풀이 
    # int result = 0;
    # int len = columnTitle.length();
    # for (int i = 0; i < len; i++) {
    #     int idx = len-1-i;
    #     result += Math.pow(26,i)*(columnTitle.charAt(idx)-'A'+1);
    # }
    # return result;