# 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948?language=python3
# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수
def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer += "*"
    answer += phone_number[-4:]
      
    return answer

print(solution("01033334444")) # return "*******4444"