data = [2, 4, 5, 11, 3]
test = 0
for i in data:
    if i > 10: 
        test = 1 
    break 
if(test == 0): print('10 보다 큰 수 없음')
# =============== for else 문을 통해 몇줄 줄일 수 있음
for j in data:
    if i >10:
        break
else: print('10 보다 큰 수 없음')

# 보통 프로그래밍 언어에서 'else'라고 하면 if와 함께 오는 경우가 거의 대부분입니다.
# 하지만 파이썬에서는 for 문과도 함께 쓰기도 합니다.
# for와 함께 쓰는 else는, for문이 중간에 break 등으로 끊기지 않고,
# 끝까지 수행 되었을 때 수행하는 코드를 담고 있습니다.
# 코딩을 하다 보면 for문이 중간에 break 되었는지, 되어있지 않는지 판별해야 되는 경우가 많이 있습니다.
# 테스트 변수를 둬서 확인하는 등으로 처리합니다
# 파이썬에서는 else의 사용으로 간단하게 해결할 수 있습니다.
# if문에 else를 사용하듯이 else를 사용하게 됩니다.
# else의 들여쓰기는 for와 일치해야 합니다.

# 출처: https://harryp.tistory.com/317 [Park's Life]