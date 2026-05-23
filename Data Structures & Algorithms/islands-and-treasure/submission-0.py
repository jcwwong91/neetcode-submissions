class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        spots = list()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    spots.append((i, j))
        
        distance = 0
        while len(spots) > 0:
            distance += 1
            next_spots = list()
            for (i, j) in spots:
                for (ii, jj) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 <= ii < len(grid) and 0 <= jj  < len(grid[ii]) and grid[ii][jj] == 2147483647:
                        grid[ii][jj] = distance
                        next_spots.append((ii,jj))
            spots = next_spots
        # print(grid)

                    
