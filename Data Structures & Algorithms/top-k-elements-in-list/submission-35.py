class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Count frequencies - O(N)
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        # 2. Convert to a list of tuples (frequency, value) - O(N)
        # We use negative frequency to simulate a Max-Heap using our Min-Heap logic,
        # OR we just build a Max-Heap. Let's build a Max-Heap for "Top K".
        heap = [[f, val] for val, f in freqs.items()]
        n = len(heap)
        
        # 3. Build Max-Heap - O(N)
        # Start from the last non-leaf node and heapify down
        for i in range((n // 2) - 1, -1, -1):
            self.heapifyDown(heap, i, n)
            
        # 4. Extract Max K times - O(K log N)
        res = []
        for i in range(k):
            # Swap root with last element
            heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
            max_val = heap.pop()
            res.append(max_val[1])
            # Restore heap property for the smaller heap
            self.heapifyDown(heap, 0, len(heap))
            
        return res

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