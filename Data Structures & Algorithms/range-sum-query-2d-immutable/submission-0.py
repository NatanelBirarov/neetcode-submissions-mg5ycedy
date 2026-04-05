class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSumMatrix = self.constructPrefixMatrix(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1 = row1 + 1, col1 + 1
        row2, col2 = row2 + 1, col2 + 1  
        return (
            self.prefixSumMatrix[row2][col2] - 
            self.prefixSumMatrix[row1 - 1][col2] -
            self.prefixSumMatrix[row2][col1 - 1] + 
            self.prefixSumMatrix[row1 - 1][col1 - 1]
            )

    def constructPrefixMatrix(self,matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        prefixSumMatrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefixSumMatrix[i][j] = (matrix[i - 1][j - 1] + 
                prefixSumMatrix[i - 1][j] +
                prefixSumMatrix[i][j-1] - 
                prefixSumMatrix[i-1][j-1])
                
        print(prefixSumMatrix)
        return prefixSumMatrix


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)