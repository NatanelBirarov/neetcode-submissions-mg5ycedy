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
            self.push(topK, (freqs[num], num))
            if (len(topK)) > k:
                self.pop(topK)        
        res = []
        for i in range(k):
            res.append(self.pop(topK)[1])
        return res

    def pop(self, heap):
        if not heap:
            return      
        heapLen = len(heap)
        heap[0], heap[heapLen - 1] = heap[heapLen - 1], heap[0]
        minVal = heap.pop()
        self.heapifyDown(heap)
        print("pop:", heap)
        return minVal

    def push(self, heap, val):
        heap.append(val)
        if len(heap) == 1:
            return
        self.heapifyUp(heap)
        print("push:", heap)
    
    def heapifyDown(self, heap):
        n = len(heap)
        i = 0
        while i < n:
            left = 2 * i + 1
            right = 2 * i + 2
            if left >= n: return
            if right >= n:
                min_child = left
            else: 
                min_child = right if heap[right][0] < heap[left][0] else left
            if heap[i][0] > heap[min_child][0]:
                heap[i], heap[min_child] = heap[min_child], heap[i]
                i = min_child
            else:
                break

    def heapifyUp(self, heap):
        i = len(heap) - 1
        while i > 0:
            parent = ((i - 1) // 2)
            if heap[i][0] < heap[parent][0]:
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break
                

