class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        for i in range(len(nums)):
            ans[i] = ans[len(nums)+i] = nums[i]
        return ans

answer = Solution()
print(answer.getConcatenation([1,4,1,2]))

