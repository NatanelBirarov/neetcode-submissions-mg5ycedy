class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            print(target - num)
            if target - num in indices:
                return [indices[target - num], i]
            indices[num] = i