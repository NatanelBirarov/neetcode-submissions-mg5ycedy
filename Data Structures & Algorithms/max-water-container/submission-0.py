class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i, j = 0, len(heights) - 1
        while i < j:
            min_height = min(heights[i], heights[j])
            area = (j - i) * min_height
            max_area = max(area, max_area)
            if min_height == heights[i]:
                i += 1
            else:
                j -= 1
        return max_area