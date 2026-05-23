

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgemap = dict()
        for n1, n2 in edges:
            if n1 == n2:
                return False
            if n1 not in edgemap:
                edgemap[n1] = set()
            if n2 not in edgemap:
                edgemap[n2] = set()
            edgemap[n1].add(n2)
            edgemap[n2].add(n1)
        
        seen = [False] * n
        process = [(0,0)]
        while process:
            node, source = process.pop()
            if seen[node]:
                # print("dupe found", node)
                return False
            seen[node] = True
            for neighbor in edgemap.get(node, set()):
                if neighbor == source:
                    continue
                # print("adding", neighbor, "from", node)
                process.append((neighbor, node))

        # print(seen)
        for v in seen:
            if not v:
                return False

        return True