class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rem = k % n
        jumps = start = 0
        while jumps < n:
            i = start
            prev = nums[start]
            while True:
                index = (i + rem) % n
                prev, nums[index] = nums[index], prev
                i = index
                jumps += 1

                if start == i:
                    break
            start += 1
    
        