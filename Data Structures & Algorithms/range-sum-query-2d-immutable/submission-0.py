class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.values = list()
        for i in range(len(matrix)):
            row = matrix[i]
            self.values.append([0] * len(row))
            total = 0
            for j in range(len(row)):
                total += row[j]
                if i == 0:
                    self.values[0][j] = total
                else:
                    self.values[i][j] = total + self.values[i-1][j]

        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.values[row1-1][col2] if row1 > 0 else 0
        left = self.values[row2][col1-1] if col1 > 0 else 0
        corner = self.values[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return self.values[row2][col2] - top - left + corner
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)