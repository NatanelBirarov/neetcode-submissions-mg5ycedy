class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        test = len(nums) // 2

        for num in nums:
            count[num] += 1
            if count[num] > test:
                return num


        # res = count = 0

        # for num in nums:
        #     if count == 0:
        #         res = num
        #     count += (1 if num == res else -1)
        # return res