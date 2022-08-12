# https://leetcode.com/problems/majority-element/
# 169. Majority Element
# https://jaime-note.tistory.com/66 : 리스트노드 사용법

# 문제에서 요구하는것은
# { 0, 0, 1, 1, 2, 2, 3, 3, 3 } 같은 다수의 숫자를 찾으라 가 아닌
# { 0, 1, 3, 3, 2, 2, 2, 2, 2 } 같은 반 수를 넘는 숫자를 찾으라 이다.
# 따라서 다수의 숫자인지 아닌지를 고려할 필요없이
# 1/2를 넘느냐 안넘느냐만 판단하면 된다.

# 어느 숫자가 그 배열에 반 이상이면 그 숫자가 정답.

# Time Limit Exceeded
# class Solution:
#     def majorityElement(self, nums):
#         max_Count = max(nums, key=nums.count) # 가장 많은 개수를 가진 수
#         return max_Count
#     print(majorityElement(1,[-1,1,1,1,2,1]))
    

    # 딕셔너리를 만들고 nums list를 한개씩 뺴면서 dic에 있는지 확인 하면서 카운트
    #  if dic[n] > len(nums)/2  여기서 n의 개수가 nums 리스트 /2 보다 크다면 return n
class Solution:
    def majorityElement(self, nums):
        dic = {}
        for n in nums :
            if n in dic :
                dic[n] += 1
            else :
                dic[n] = 1
                
            if dic[n] > len(nums)/2 :
                return n


    print(majorityElement(1,[-1,1,1,1,2,1]))