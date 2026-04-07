class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i, fixed in enumerate(nums):
            if fixed > 0:
                break

            if i > 0 and nums[i - 1] == fixed:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = fixed + nums[l] + nums[r]
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    triplets.append([fixed, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 

        return triplets
            


    