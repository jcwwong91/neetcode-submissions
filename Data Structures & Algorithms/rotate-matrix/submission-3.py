class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # i = 0
        # j = 1
        # print(int((len(matrix) + 1) / 2), (len(matrix) % 2))
        # printMatrix(matrix)

        def rotate(i, j):
            """
            ul = matrix[i][j]
            ur = matrix[j][n-i]
            dr = matrix[n-i][n-j]
            dl = matrix[n-j][i]
            """ 

            tmp =  matrix[n-i][n-j]
            matrix[n-i][n-j] = matrix[j][n-i]
            matrix[j][n-i] = matrix[i][j]
            matrix[i][j] = matrix[n-j][i]
            matrix[n-j][i] = tmp
            # print(i, j , ul, ur, dr, dl)

        n = len(matrix) - 1
        rlen = len(matrix)//2 + (1 if len(matrix) % 2 else 0)
        for i in range(rlen):
            for j in range(len(matrix)//2):
                rotate(i,j)
                # printMatrix(matrix)


def printMatrix(matrix):    
    print("------")
    for row in matrix:
        print(row)
                