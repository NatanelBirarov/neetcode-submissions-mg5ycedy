class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        max_val = (0)
        l = r = 0
        
        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            
            if l > dq[0]:
                dq.popleft()

            if r + 1 >= k:
                res.append(nums[dq[0]])
                l += 1
            r += 1

        return res

        # self.indices = defaultdict(set)
        # result = []
        # max_heap = []
        # heapq.heapify_max(max_heap)
        # for i in range(len(nums)):
        #     heapq.heappush_max(max_heap, (nums[i], i))
        #     print(max_heap)
        #     if i >= k - 1:
        #         print(i - k)
        #         while max_heap[0][1] <= i - k:
        #             heapq.heappop_max(max_heap)
        #         result.append(max_heap[0][0])
        # return result



