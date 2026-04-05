import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
                
        print(freqs)
        topK = []
        for num in freqs.keys():
            heapq.heappush(topK, (freqs[num], num))
            if (len(topK)) > k:
                heapq.heappop(topK)

        res = []
        for i in range(k):
            res.append(heapq.heappop(topK)[1])
        return res

