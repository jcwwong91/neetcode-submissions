class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(n):
            if n == parent[n]:
                return n
            parent[n] = find(parent[n])
            return parent[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            parent[n1] = parent[n2] = parent[p1] = parent[p2] = min(p1, p2)
            return True

        for n1, n2 in edges:
            # print(parent, n1, n2)
            if not union(n1, n2):
                return [n1, n2]

        return []