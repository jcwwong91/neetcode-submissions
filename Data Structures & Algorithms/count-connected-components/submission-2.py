class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))

        def get_parent(n):
            if parents[n] == n:
                return n
            parents[n] = get_parent(parents[n])
            return parents[n]

        def set_parent(n1, n2):
            p1, p2 = get_parent(n1), get_parent(n2)

            p = min(p1, p2) 
            parents[n1] = parents[n2] = parents[p1] = parents[p2] = p
            # print(n1, n2, "parents", parents)

        for n1, n2 in edges:
            set_parent(n1, n2)

        heads = set()
        for i in range(n):
            p = get_parent(i)
            # print("node", i, "parent", p)
            heads.add(p)
        
        return len(heads)
        