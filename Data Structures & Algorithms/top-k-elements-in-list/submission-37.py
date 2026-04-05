import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        heap = [[freqs[num], num] for num in freqs.keys()]
        self.buildHeap(heap) 
        print(heap)

        res = []
        for i in range(k):
            n = len(heap) - 1
            heap[0], heap[n] = heap[n], heap[0]
            num = heap.pop()
            self.heapifyDown(heap, 0, len(heap))
            res.append(num[1])
        return res

    def buildHeap(self, heap):
        n = len(heap)
        for i in range((n // 2) - 1, -1, -1):
            self.heapifyDown(heap, i, n)
    
    def heapifyDown(self, heap, i, n):
        """Standard Max-Heapify Down"""
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            # Compare with left child
            if left < n and heap[left][0] > heap[largest][0]:
                largest = left
            
            # Compare with right child
            if right < n and heap[right][0] > heap[largest][0]:
                largest = right
                
            if largest != i:
                heap[i], heap[largest] = heap[largest], heap[i]
                i = largest
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
    
    def pop(self, heap):
        if not heap:
            return      
        heapLen = len(heap)
        heap[0], heap[heapLen - 1] = heap[heapLen - 1], heap[0]
        minVal = heap.pop()
        self.heapifyDown(heap)
        return minVal

    def push(self, heap, val):
        heap.append(val)
        if len(heap) == 1:
            return
        self.heapifyUp(heap)
                

