class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countObj = {}
        for num in nums:
            if num in countObj:
                return True
            countObj[num] = 0
        return False
             