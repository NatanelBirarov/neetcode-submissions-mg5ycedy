class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        i = 0
        j = 1
        k = 1

        while i < n and j < n:
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                k += 1
            j += 1

        # while i < len(nums):
        #     if nums[i] == nums[i - 1]:
        #         break
        #     i += 1
        #     k += 1
        
        # while i < len(nums):
        #     if nums[i] != nums[i - 1]:
        #         nums[i - 1] = nums[i]
        #         k += 1
        #     i += 1
        
        return k
