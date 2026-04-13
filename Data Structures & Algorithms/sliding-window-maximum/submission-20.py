class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

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



