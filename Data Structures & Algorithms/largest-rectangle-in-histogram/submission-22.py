class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = heights[0]
        min_height = heights[0]
        for i in range(n):
            w = 0
            min_height = min(min_height, heights[i])
            while stack and heights[stack[-1]] > heights[i]:
                v = stack.pop()
                w = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, heights[v] * w)     

            stack.append(i)
        
        r = n
        while stack:
            v = stack.pop()
            l = stack[-1] if stack else 0
            h = heights[v]
            w = r - l - 1 if stack else r
            max_area = max(max_area, h * w)

        return max_area



        # stack = []
        # n = len(heights)

        # left = [-1] * n
        # for i in range(n):
        #     while stack and heights[stack[-1]] >= heights[i]:
        #         stack.pop()
        #     if stack:
        #         left[i] = stack[-1]
        #     stack.append(i)

        # stack = []
        # right = [n] * n
        # for i in range(n - 1, -1 ,-1):
        #     while stack and heights[stack[-1]] >= heights[i]:
        #         stack.pop()
        #     if stack:
        #         right[i] = stack[-1]
        #     stack.append(i)

        # max_area = 0
        # for i in range(n):
        #     left[i] += 1
        #     right[i] -= 1
        #     max_area = max(max_area, heights[i] * (right[i] - left[i] + 1))

        # return max_area