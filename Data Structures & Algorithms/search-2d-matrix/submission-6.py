import numpy as np

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        print(np.shape(matrix))
        while l <= r:
            mid = l + ((r - l) // 2)
            i = mid // len(matrix[0])
            j = mid % len(matrix[0])
            if matrix[i][j] == target:
                return True

            elif matrix[i][j] <= target:
               l = mid + 1
            else:
                r = mid - 1

        return False