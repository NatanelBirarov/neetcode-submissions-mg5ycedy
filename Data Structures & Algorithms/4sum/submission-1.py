class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = []
        print(nums)
        for i, fixed1 in enumerate(nums):
            if i > 0 and nums[i - 1] == fixed1:
                continue
            for j in range(len(nums) - 1, i, -1):
                fixed2 = nums[j]
                if j < len(nums) - 1 and nums[j + 1] == fixed2:
                    continue
                l = i + 1
                r = j - 1
                fixed = fixed1 + fixed2
                while l < r:
                    print(i, l, r, j)
                    curr_sum = fixed + nums[l] + nums[r]
                    if curr_sum < target:
                        l += 1
                    elif curr_sum > target:
                        r -= 1
                    else:
                        quads.append([fixed1, fixed2, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1 

        return quads
            