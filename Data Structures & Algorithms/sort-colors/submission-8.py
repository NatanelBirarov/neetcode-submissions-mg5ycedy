class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # n = len(nums)
        # for j in range(n):
        #     if nums[j] == 0 and i != j:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        # for j in range(i, n):
        #     if nums[j] == 1:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1

        i, j = 0, 0
        k = len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1;
            else:
                j += 1
        