class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        queue = list()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    break
            if queue:
                break

        ret = 0
        seen = set()
        while queue:
            i, j = queue.pop(0)
            if (i, j) in seen:
                continue
            seen.add((i, j))
            perim = 0
            for ii, jj in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
                if (ii, jj) in seen:
                    continue
                if ii < 0 or ii >= len(grid) or jj <0 or jj >= len(grid[i]) or grid[ii][jj] == 0:
                    perim += 1
                    continue
                
                queue.append((ii, jj))
            # print("perim", i, j, perim)
            ret += perim
        return ret

                


    