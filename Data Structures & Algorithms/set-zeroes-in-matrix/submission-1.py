class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        def print_matrix(id):
            print(id)
            for row in matrix:
                print(row)

        rowZero = False
        colZero = False

        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                if matrix[i][j] == 0:
                    if i == 0:
                        rowZero = True
                    if j == 0:
                        colZero = True

                    if i > 0 and j > 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        

        #print_matrix("1-----")

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        
        # print_matrix("1.5-----")
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        # print_matrix("2-----")

        if rowZero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if colZero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        # print_matrix("3-----")
        
        