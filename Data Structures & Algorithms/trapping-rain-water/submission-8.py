class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = []
        max_trapped = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                m = height[stack.pop()]
                if stack:
                    r = height[i]
                    l = height[stack[-1]]
                    h = min(r, l) - m
                    w = i - stack[-1] - 1
                    max_trapped += h * w
            stack.append(i)

        return max_trapped



