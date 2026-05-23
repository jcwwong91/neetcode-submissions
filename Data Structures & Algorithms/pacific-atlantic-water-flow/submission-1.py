class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = list()
        atlantic = list()

        pacificSeen = set()
        atlanticSeen = set()
        for i in range(len(heights[0])):
            pacific.append((0, i))
            pacificSeen.add((0, i))
            atlantic.append((len(heights)-1, i))
            atlanticSeen.add((len(heights)-1, i))
        for j in range(len(heights)):
            pacific.append((j, 0))
            pacificSeen.add((j, 0))
            atlantic.append((j, len(heights[0])-1))
            atlanticSeen.add((j, len(heights[0])-1))

        while pacific:
            i, j = pacific.pop()
            curHeight = heights[i][j]
            for ii, jj in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
                if ii < 0 or ii >= len(heights) or jj < 0 or jj >= len(heights[0]) or (ii,jj) in pacificSeen:
                    continue # Invalid point
                potHeight = heights[ii][jj]
                if potHeight >= curHeight:
                    # print("pacific", ii, jj, "from", i, j)
                    pacificSeen.add((ii, jj))
                    pacific.append((ii, jj))

        while atlantic:
            i, j = atlantic.pop()
            curHeight = heights[i][j]
            for ii, jj in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
                if ii < 0 or ii >= len(heights) or jj < 0 or jj >= len(heights[0]) or (ii,jj) in atlanticSeen:
                    continue # Invalid point
                potHeight = heights[ii][jj]
                if potHeight >= curHeight:
                    # print("atlantic", ii, jj, "from", i, j)
                    atlanticSeen.add((ii, jj))
                    atlantic.append((ii, jj))

        common = atlanticSeen & pacificSeen
    
        ret = list()
        for i, j in common:
            ret.append([i, j])

        return ret