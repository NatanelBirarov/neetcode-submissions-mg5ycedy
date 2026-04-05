class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def mergeSort(self, nums: List[int]):
        if len(nums) == 0 or len(nums) == 1:
            return nums
        
        m = len(nums) // 2
        left = self.mergeSort(nums[:m])
        right = self.mergeSort(nums[m:])
        return self.merge(left, right)
        
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        i, j = 0, 0
        sortedArr = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sortedArr.append(left[i])
                i += 1
            else:
                sortedArr.append(right[j])
                j += 1

        while i < len(left):
            sortedArr.append(left[i])
            i += 1
        
        while j < len(right):
            sortedArr.append(right[j])
            j += 1

        return sortedArr