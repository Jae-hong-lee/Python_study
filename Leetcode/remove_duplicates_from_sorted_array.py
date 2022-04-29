# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# 내림차순으로 정렬된 정수 배열이 주어지며, 각 고유 요소가 한 번만 나타나도록 중복을 제자리에서 제거합니다. 요소의 순서는 동일하게 유지. (111223 -> 123 순서는 동일)
# 배열길이 변경불가, 배열의 첫번째 부분에 결과 출력 (중복아닌 수 개수?)
#  제자리에서 입력 배열 을 수정하여 이 작업을 수행해야 합니다 .
# 정렬된 수 배열. 중본된 수 제거한 길이 return?
# 배열길이 건들지마라 , 중복 지우고 남은수 return

# O(1) – 상수 시간 : 문제를 해결하는데 오직 한 단계만 처리함.  # for문 두개 쓰면 안된다는 소리 같음
# 조건문 + for 는 시간복잡도???

# 1 wrong Answer output : [1,1] expected [1,2]
# _ 이거로 뒤에를 바꾸는 게 아닌 중복수를 제거한 숫자 갯수 return, 그리고 앞에부터 중복숫자 확인하겠다는 뜻.
# 뒤에 나오는 숫자는 무시한다고 한다.
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         if len(nums)==0: return 0
#     # 중복된 수 카운트.
#         count =0
#         for i in range(1,len(nums)):
#             if nums[i] != nums[i-1]:
#                 continue
#             else:
#                 count+=1
        
#         print(nums)
#         return len(nums)-count

# l = Solution()
# print(l.removeDuplicates([1,1,2])) #2, [1,2,_]
# print(l.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5, [0,1,2,3,4,_,_,_,_,_]


# 2
# 중복된 수를 뒤로 보내던 팝한다.?
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         if len(nums)==0: return 0
#         count =0
#         for i in range(1,len(nums)):
#             if nums[i] != nums[i-1]:
#                 continue
#             else:
#                 count+=1
#                 # x = nums.pop(-1) 앞에 빼는거 뭐였냐
#                 x = nums.pop(0)
#                 nums.append(x)
#         print(nums)
#         return len(nums)-count


# l = Solution()
# print(l.removeDuplicates([1,1,2])) #2, [1,2,_] 
# print(l.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5, [0,1,2,3,4,_,_,_,_,_]

# 3
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         if len(nums)==0: return 0
#         count =0
#         num = list(nums)
#         for i in range(1,len(nums)):
#             if nums[i] != nums[i-1]:
#                 continue
#             else:
#                 count+=1
#                 x = num.pop(count)
#                 # x = nums.pop(-1) 앞에 빼는거 뭐였냐
#                 num.append(x)
#         print(num)
#         return len(nums)-count
# # num -> nums , nums-> num 변경 후 제출
# # [1,2,2] 오류 221 나옴.
# l = Solution()
# print(l.removeDuplicates([1,2,2])) #2, [1,2,_] 
# print(l.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5, [0,1,2,3,4,_,_,_,_,_]


# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         if len(nums)==0: return 0
#     # 중복된 수 카운트.
#         count =0
#         for i in range(1,len(nums)):
#             if nums[i] != nums[i-1]:
#                 continue
#                 # x= nums[i]
#                 # nums[len(nums)-1] = x
#             else:
#                 count+=1
#                 x = nums.pop(i)
#                 nums.append(x)
#         print(nums)
#         return len(nums)-count

# l = Solution()
# print(l.removeDuplicates([1,1,2])) #2, [1,2,_]
# print(l.removeDuplicates([1,2,2])) #2, [1,2,_]
# print(l.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5, [0,1,2,3,4,_,_,_,_,_]

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)==0: return 0
        count =0
        num = list(nums)
        for i in range(1,len(num)):
            if num[i] != num[i-1]:
                continue
            else:
                x = nums.pop(i- count)
                #x = nums.pop(count-1)
                nums.append(x)
                count+=1
        #print(num)
        return len(nums)-count
l = Solution()
print(l.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5, [0,1,2,3,4,_,_,_,_,_]
# 팝해서 뒤로 돌려놓는 인덱스 찾느라 힘들었음 (ex: 뒤로 다시 붙여주면 방이 하나씩 앞으로 댕겨진다.)
# 그냥 nums 리스트를 새로 num이라는 리스트에 지정해주고
# num으로 앞뒤문자 판별해서 같지 않으면 넘기고, 같다면 x 라는 변수는 nums에서 
# i-count 번째 수 팝! 후 카운트 세고 nums에 추가.
# count는 뒤로 돌리는 수 이면서, 중복되는 수에 갯수
# 통과
# 런타임: 213ms로 정렬된 배열에서 중복 제거를 위한 Python3 온라인 제출의 13.19%보다 빠릅니다.
# 메모리 사용량: 15.5MB로 정렬된 배열에서 중복 제거를 위한 Python3 온라인 제출의 96.63% 미만입니다.