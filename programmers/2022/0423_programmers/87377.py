# 교점에 별 만들기
# https://programmers.co.kr/learn/courses/30/lessons/87377

# Ax + By + C = 0 으로 표현할 수 있는 n개의 직선이 주어질 때,
# 이 직선의 교점 중 정수 좌표에 별을 그리려 합니다.

#  AD - BC = 0인 경우 두 직선은 평행 또는 일치합니다.
# Ax + By + E = 0
# Cx + Dy + F = 0
# 두 직선의 교점이 유일하게 존재할 경우, 그 교점은 다음과 같습니다.

# 줄긋기를 어떻게 해야하나?? = matplotlib 선형방정식 x축, y축 그리기 xxxxx 진짜 그래프그리기임;
# 벡터를 사용하는 식이라는데..?
# 일반적으로 벡터는 화살표로 표현합니다. 화살표가 가리키는 쪽은 방향을 나타내며 화살표의 길이는 크기를 나타냅니다.
# https://ko.khanacademy.org/computing/computer-programming/programming-natural-simulations/programming-vectors/a/intro-to-vectors
# 진짜 벡터 쓰는거였네;;;

# 그래프 두개 만들어서 x좌표 y좌표 찍고 중복된 거에는 별 찍고 아니면 . 찍기 할려고 했음.
# 포기한 이유 : 아래쪽 가면 그냥 중복값 판별해서 별찍기가 아님 -> 최소 사각형을 뽑아내야한다.

# 0일때랑 / (-1,1), (1,1) / 일때 별찍는거 보고 아니라고 느낌
# Ax + By + E , Cx + Dy + F
# x = BF - ED / AD -BC
# y = EC -AF / AD - BC

def solution(line):
    star_list = [] # 교점 리스트
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a*d - b*c !=0:
                x,y = (b*f-e*d)/(a*d - b*c) , (e*c-a*f)/(a*d - b*c)
                if x.is_integer() and y.is_integer():
                    # 변수가 정수인지 확인
                    x,y = int(x),int(y)
                    # 소수점 지우기?
                    if (x,y) not in star_list:
                        star_list.append((x,y))
    # 3. 2차원 평면상의 좌표를 2차원 배열의 좌표로 찍어내려면 
    # x, y = abs(y_max-b) , abs(x_min-a)의 공식으로 구할 수 있다.

    # 최소직사각형.
    x_min, x_max, y_min, y_max = min(star_list)[0],max(star_list)[0],min(star_list,key = lambda x: x[1])[1],max(star_list,key = lambda x: x[1])[1]
    star = [['.']*(abs(x_max-x_min)+1) for _ in range((abs(y_max-y_min)+1))]
    for s in star_list:
        a,b = s
        x,y = abs(y_max-b) , abs(x_min-a)
        star[x][y] = '*'
    for i,v in enumerate(star):
        star[i] = ''.join(v)
    return star
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))




def solution(line):
    pos = []
    answer = []
    n = len(line)

    x_min, y_min = int(1e15),int(1e15)
    x_max, y_max = -int(1e15), -int(1e15)
    
    for i in range(n):
        a,b,e = line[i]
        for j in range(i+1,n):
            c,d,f = line[j]
            if a*d == b*c :
                continue
            x = (b*f-e*d) / (a*d-b*c)
            y = (e*c-a*f) / (a*d-b*c)

            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x,y])
                if x_min > x :
                    x_min = x
                if y_min > y:
                    y_min = y
                if x_max < x:
                    x_max = x
                if y_max < y :
                    y_max = y

    x_len = x_max-x_min+1
    y_len = y_max-y_min+1
    arr = [['.']*x_len for _ in range(y_len)]

    for star_x, star_y in pos:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        arr[ny][nx]='*'

    for i in range(len(arr)-1,-1,-1):
        answer.append(''.join(arr[i]))

    return answer
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))