class Solution:
    def openLock(self, deadends: List[str], rt: str) -> int:
        locks = set()
        for d in deadends:
            v = (int(d[0]), int(d[1]), int(d[2]), int(d[3]))
            locks.add(v)
        target = (int(rt[0]), int(rt[1]), int(rt[2]), int(rt[3]))
        if target in locks or (0, 0, 0, 0) in locks:
            return -1
        path = {(0,0,0,0): 0}
        queue = list()

        queue.append((0, 0, 0, 0))

        while queue:
            s = queue.pop(0)
            for i in range(4):
                for j in [1, -1]:
                    v = list(s)
                    v[i] = (v[i] + j)%10
                    t = tuple(v)
                    if t not in locks and t not in path:
                        path[t] = path[s] + 1
                        queue.append(t)
                    if t == target:
                        return path[t]

        return -1
