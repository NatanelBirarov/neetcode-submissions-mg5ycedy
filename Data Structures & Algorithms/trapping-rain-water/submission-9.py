class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        max_trapped = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                max_trapped += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                max_trapped += maxR - height[r]
        
        return max_trapped

        # if not height:
        #     return 0
        # stack = []
        # max_trapped = 0
        # for i in range(len(height)):
        #     print(i, stack)
        #     while stack and height[i] >= height[stack[-1]]:
        #         m = height[stack.pop()]
        #         if stack:
        #             r = height[i]
        #             l = height[stack[-1]]
        #             h = min(r, l) - m
        #             w = i - stack[-1] - 1
        #             max_trapped += h * w
        #     stack.append(i)

        # return max_trapped



