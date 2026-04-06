class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1
        # not_neg = []
        # for num in nums: 
        #     if num > 0:
        #         not_neg.append(num)
        # if not not_neg:
        #     return 1 
        # not_neg_set = set(not_neg)
        # min_num = min(not_neg)
        # if min_num > 1:
        #     return 1       
        # else:
        #     curr_num = min_num + 1
        #     while curr_num in not_neg_set:
        #         curr_num += 1
        #     print(curr_num)
        #     return curr_num
