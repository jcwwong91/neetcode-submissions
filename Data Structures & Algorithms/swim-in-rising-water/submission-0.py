class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        heap = list()
        visited = set()

        def visit(i, j):
            # print("visiting", i, j, grid[i][j])
            visited.add((i,j))

            for (ii, jj) in [(i + 1, j), (i - 1, j), (i, j+1), (i, j-1)]:
                if ii < 0 or ii >= len(grid) or jj <0 or jj >= len(grid):
                    continue
                
                # print("pushing", ii, jj)
                heapq.heappush(heap, (grid[ii][jj], ii, jj))

        visit(0, 0)
        maxTime = grid[0][0]
        while len(heap) > 0:
            time, i, j = heapq.heappop(heap)
            maxTime = max(maxTime, time)

            if (i,j) in visited:
                continue
            visit(i,j)
            if i == len(grid) -1 and j == len(grid) -1:
                break
            

        return maxTime




        