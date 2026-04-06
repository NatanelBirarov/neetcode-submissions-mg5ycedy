class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i += 1
                continue
                
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
    
        for i in range(n):
            if nums[i] == 0 or nums[i] != i + 1:
                return i + 1

        return n + 1
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
        