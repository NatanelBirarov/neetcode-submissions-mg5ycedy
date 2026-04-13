class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        self.indices = defaultdict(set)
        result = []
        max_heap = []
        heapq.heapify_max(max_heap)
        for i in range(len(nums)):
            heapq.heappush_max(max_heap, (nums[i], i))
            if i >= k - 1:
                while max_heap[0][1] <= i - k:
                    heapq.heappop_max(max_heap)
                result.append(max_heap[0][0])
        return result



