#1. leetcode twosum
print("leetcode submissions:")

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in new_dict:
                return [new_dict[target - nums[i]], i]
            new_dict[nums[i]] = i


