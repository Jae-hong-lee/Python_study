# 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969?language=python3
# n과 m은 각각 1000 이하인 자연수입니다.
n, m = map(int, input().strip().split(' '))

for i in range(m):
    for e in range(n):
        print("*",end='')
        
    print()

#줄마다 몇개의 *을 출력!
#이중 for문??