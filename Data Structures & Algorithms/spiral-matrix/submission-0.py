class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = list()

        rows = len(matrix)
        cols = len(matrix[0])
        spirals = (min(rows, cols) // 2)

        for i in range(spirals):
            # top
            for j in range(i, cols-i):
                ret.append(matrix[i][j])

            
            # right
            for j in range(i+1, rows-i):
                ret.append(matrix[j][cols-i-1])

            # bottom
            for j in range(cols-i-2, i-1, -1):
                ret.append(matrix[rows-i-1][j])

            # left
            for j in range(rows-i-2,i, -1):
                ret.append(matrix[j][i])

        # print(ret)
        if min(rows, cols) % 2:
            i = spirals
            if rows < cols:
                for j in range(i, cols-i):
                    ret.append(matrix[i][j])
            elif cols < rows:
                for j in range(i, rows-i):
                    ret.append(matrix[j][cols-i-1])
            else:
                ret.append(matrix[i][i])


        return ret


        
            

        