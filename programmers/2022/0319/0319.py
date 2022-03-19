# [1차] 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679

# 입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.
# 높이, 폭 , 배치정보

# 같은 블록은 여러 2×2에 포함될 수 있으며, 
# 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.

# 2*2 사각형 지우고, 위에서 아래로 떨어짐

# 2*2 = board(0,0) (1,0) (0,1) (1,1)
# graph 값이 변화 되면 변화된 값이 들어있는 board 에 위치에 있는 것들을 지우고
# 아래로 내리고 다시 반복?
# 아래로 내리는 로직 생각....
def solution(m, n, board):
    answer = 0
    graph = [[0 for _ in range(n)] for _ in range(m)] # 확인. 1이되면 BOARD지우기.    

    for i in range(m-1):
        for j in range(n-1):
            if board[i+1][j] == board[i][j] and board[i][j+1] == board[i][j] and board[i+1][j+1] == board[i][j]:
                graph[i][j], graph[i+1][j], graph[i][j+1], graph[i+1][j+1] = 1,1,1,1
                # TypeError: cannot unpack non-iterable int object
            #if graph[i][j] == 1:
                # board.pop([i][j])
                # print(board[i][j])
            #    x = board[i][j]
            #    board[i].replace(x,' ')

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                x = board[i][j]
                board.replace(x, ' ')
                # X , board 를 list 로 만들자.
                # 2차원배열로 바꾸자.
    print(board)
    # 이동하는 문항? , 반복 구현XX
    
    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))


# def solution(m, n, board):
#     answer = 0
#     graph = [[0 for _ in range(n)] for _ in range(m)] # 확인. 1이되면 BOARD지우기.    
#     # print(graph)
#     # print(board)
#     # board = for _ in range(n): #폭 
#     # for _ in range(m):        #길이      #board 가 주어져있으니 만들필요 X
    
#     # try:
#     for i in range(m):
#         for j in range(n):
#             # if board[0,0] == board[m,n+1] and 
#             # if board[i,j] == board[i,j+1] and board[i,j] == board[i+1,j] and board[i,j] == board[i+1,j+1]:
#             if board[i+1][j] == board[i][j] and board[i][j+1] == board[i][j] and board[i+1][j+1] == board[i][j]:
#                 graph[i][j],graph[i+1][j],graph[i][j+1],graph[i+1][j+1] = 1
#     # except:
#     #     continue    #try 문으로 에러떠도 돌릴라했는데ㅔ continue 가 안먹힘.

#     # TypeError: list indices must be integers or slices, not tuple
#     # IndexError: string index out of range 
#     # 인덱스 범위가 벗어나짐, 바깥쪽 아래쪽 타일들...

#     print(graph)
#     return answer

# print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
# # answer 14 , 15