class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        if nums[0] == 0:
            i = 1
        n = len(nums)
        while i < n and j < n:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        j = i
        while i < n and j < n:
            if nums[j] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums
