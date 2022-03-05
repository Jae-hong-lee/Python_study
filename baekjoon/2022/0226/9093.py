# 단어 뒤집기
# https://www.acmicpc.net/problem/9093

# import sys
# input = open('python/baekjoon/input2.txt','r')
# T = int(input.readline())
# # str = input.readline()
# # str2 = input.readline()
# # print(T,str,str2)
# for _ in range(T):
#     str = input.readline().rstrip() # 문자제거
#     word = list(str.split())
#     reverse_word = []
#     # print(word)
#     for i in word:
#         reverse_word += ''.join(reversed(i))
        
#     answer = " ".join(reverse_word)
#     print(reverse_word)
#     # print(answer)

# append 로 추가시켜주자.


import sys
input = open('python/baekjoon/input2.txt','r')
T = int(input.readline())
# str = input.readline()
# str2 = input.readline()
# print(T,str,str2)
for _ in range(T):
    str = input.readline().rstrip() # 문자제거
    word = list(str.split())
    reverse_word = []
    # print(word)
    for i in word:
        reverse_word.append(''.join(reversed(i)))
        
    answer = " ".join(reverse_word)
    # print(reverse_word)
    print(answer)


# 제출
import sys
T = int(sys.stdin.readline)

for _ in range(T):
    str = sys.stdin.readline().rstrip() 
    word = list(str.split())
    reverse_word = []
    
    for i in word:
        reverse_word.append(''.join(reversed(i)))
    answer = " ".join(reverse_word)
    print(answer)
    # 제출시 런타임 에러. TypeError


# 식이 잘못되었나 생각하고 슬라이싱으로 다시품
import sys
T= int(input())

for _ in range(T):
    str = sys.stdin.readline().rstrip()
    word = list(str.split())
    reverse_word = []

    for i in word:
        reverse_word.append(i[::-1])

    answer = " ".join(reverse_word)
    print(answer)