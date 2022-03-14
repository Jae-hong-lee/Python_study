# https://leetcode.com/problems/two-sum/
# 1. Two Sum
def twosum(nums,target):
    answer = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            # print(nums[i])
            # print(nums[j])
            if target == nums[i] + nums[j]:
                answer += i,j
    return answer
print(twosum([2,7,11,15],9))


# 리트코드 입력 , 다른사람 풀이
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    print(twoSum(1,[2,7,11,15],9))
    print(twoSum(2,[3,2,4],6))