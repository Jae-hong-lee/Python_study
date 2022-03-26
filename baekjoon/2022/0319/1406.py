# 에디터
# https://www.acmicpc.net/problem/1406

# 링크드리스트 단방향 구현
# https://velog.io/@woga1999/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EB%A7%81%ED%81%AC%EB%93%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8

# 제출용
# import sys
# T = int(sys.stdin.readline())

# 확인용
# input = open('python/baekjoon/input2.txt','r')
# T = int(input.readline())

# 시간복잡도 체험
# https://bnzn2426.tistory.com/112

# 첫시도 : 커서 위치를 어떻게 저장해야할까?
# input -> sys.stdin.readline()
# import sys
# sys.stdin = open('python/baekjoon/input2.txt','r')
# # input = sys.stdin.readline()
# temp = input()
# N = int(input())

# stack = [temp]
# stack2 = []
# print(stack)
# for i in range(N):
#     commands = input().rstrip().split()

#     if commands[0] == 'P':
#         stack += commands[1]
    
# print(stack)
# 커서 위치저장?


import sys
sys.stdin = open('python/baekjoon/input2.txt','r')
# input = sys.stdin.readline()
stack1 = list(input().strip())
N = int(input())

stack2 = []
for i in range(N):
    commands = input().rstrip().split()
    
    if commands[0] == 'P':
        stack1 += commands[1]

    elif commands[0] == 'L':
      if not stack1: continue # (커서가 문장의 맨 앞이면 무시됨)
      else: stack2.append(stack1.pop()) #커서를 왼쪽으로 한 칸 옮김 

    elif commands[0] == 'D':
      if not stack2: continue
      else: stack1.append(stack2.pop())

    elif commands[0] == 'B':
      if not stack1: continue # (커서가 문장의 맨 앞이면 무시됨)
      else: 
        stack1.pop()
      # 커서 왼쪽삭제, 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만,
      # 실제로 커서의 오른쪽에 있던 문자는 그대로임
# print(stack1 + list(reversed(stack2)))
print(''.join(stack1 + list(reversed(stack2))))








# 스택 / 큐
# from collections import deque
# import sys

# text = list(sys.stdin.readline().strip())
# N = int(sys.stdin.readline().strip())

# cursor = deque([])
# for i in range(N):
#   command = sys.stdin.readline().strip()
#   if command[0]== "L" and text:
#     a = text.pop()
#     cursor.appendleft(a)
#   elif command[0]=="D" and cursor:
#     a = cursor.popleft()
#     text.append(a)
#   elif command[0]=="B" and text:
#     text.pop()
#   elif command[0]== "P":
#     text.append(command[2])  
# print(''.join(text + list(cursor)))

# --------------------------
# 이중연결리스트 풀이
# import sys
# input = sys.stdin.readline
# class DList:
#     class Node:
#         def __init__(self,item,prev,link):
#             self.item = item
#             self.prev = prev
#             self.next = link
 
#     def __init__(self):
#         self.head = self.Node(None,None,None)
#         self.tail = self.Node(None,self.head,None)
#         self.head.next = self.tail
#         self.cur = self.tail
 
    # def insert(self,p,item):
    #     t = p.prev
    #     n = self.Node(item,t,p)
    #     p.prev = n
    #     t.next = n
 
    # def delete(self,x):
    #     f = x.prev
    #     r = x.next
    #     f.next = r
    #     r.prev = f
 
#     def print_list(self):
#         p = self.head.next
#         while p != self.tail:
#             if p.next != self.tail:
#                 print(p.item, end="")
#             else:
#                 print(p.item)
#             p = p.next
 
# s = list(input().rstrip())
# dl = DList()
# for i in range(len(s)):
#     dl.insert(dl.tail,s[i])
 
# for i in range(int(input())):
#     o = input()
#     if(o[0] == "L"):
#         if(dl.cur.prev.prev != None):
#             dl.cur = dl.cur.prev
#     elif(o[0] == "D"):
#         if(dl.cur.next != None):
#             dl.cur = dl.cur.next
#     elif(o[0] == "B"):
#         if(dl.cur.prev.prev != None):
#             dl.delete(dl.cur.prev)
#     else:
#         dl.insert(dl.cur,o[2])
# dl.print_list()


# --------------------------
# 서킷연결리스트 풀이. 링크드 리스트중의 하나 
# # 1. class Node 선언 부분
# class Node:
#     def __init__(self, key=None):
#         self.key = key
#         self.prev = self
#         self.next = self
#     def __str__(self):
#         return str(self.key)

# # 2. class DoublyLinkedList 선언부분
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = Node() # create an empty list with only dummy node

#     def __iter__(self):
#         v = self.head.next
#         while v != self.head:
#             yield v
#             v = v.next
#     def __str__(self):
#         return "".join(str(v.key) for v in self)
#     def splice(self, a, b, x):
#       if a == None or b == None or x == None:
#         return
#       # 1. [a..b] 구간을 잘라내기 
#       a.prev.next = b.next
#       b.next.prev = a.prev

#       # 2. [a..b]를 x 다음에 삽입하기
#       x.next.prev = b
#       b.next = x.next
#       a.prev = x
#       x.next = a
#     def moveAfter(self, a,x):    
#       self.splice(a, a, x)

#     def moveBefore(self,a,x):      
#       self.splice(a, a, x.prev) 

#     def insertBefore(self,a, key):
#       self.moveBefore(Node(key), a)
      
#     def deleteNode(self, x): # delete x
#       if x == None or x == self.head: 
#         return
#     # 노드 x를 리스트에서 분리해내기
#       x.prev.next, x.next.prev = x.next, x.prev


# import sys
# L = DoublyLinkedList()
# c = Node('|')
# c.next = L.head
# c.prev = L.head
# L.head.next = c
# L.head.prev = c
# text = list(sys.stdin.readline().strip())
# for i in text:
#   L.insertBefore(c, i)
# N = int(sys.stdin.readline().strip())  
# for i in range(N):
#   command = sys.stdin.readline().strip()
#   if command[0]== "L" and c.prev.key!=None :
#     L.moveBefore(c, c.prev)
#   elif command[0]=="D" and c.next.key!=None:
#     L.moveAfter(c, c.next)
#   elif command[0]=="B" and c.prev.key!=None:
#     L.deleteNode(c.prev)
#   elif command[0]== "P":
#     L.insertBefore(c, command[2])

# L.deleteNode(c)
# print(L)