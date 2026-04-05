class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        test = len(nums) // 3
        majorities = set()
        for num in nums:
            count[num] += 1
            if count[num] > test:
                majorities.add(num)
                if len(majorities) == 2:
                    break
        
        return list(majorities)