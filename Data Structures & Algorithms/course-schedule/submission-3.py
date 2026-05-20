
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dependencies = [0] * numCourses
        pr = dict()
        for s, d in prerequisites:
            pr[s] = pr.get(s, list())
            pr[s].append(d)
            dependencies[d] += 1

        queue = list()
        for i in range(numCourses):
            dep = dependencies[i]
            if dep == 0:
                queue.append(i)

        while len(queue) > 0:
            v = queue.pop()
            # print(v, dependencies, pr.get(v))
            for vv in pr.get(v, list()):
                dependencies[vv] -= 1
                if dependencies[vv] == 0:
                    queue.append(vv)
                # print(vv, "dep", dependencies[vv])

        
        for dep in dependencies:
            if dep > 0:
                return False
        return True
       
        