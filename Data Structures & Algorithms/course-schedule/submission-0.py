
class Node:

    def __init__(self, course):
        self.value = course
        self.children = list()
        self.parent = list()

    def add_child(self, child):
        self.children.append(child)
        child.add_parent(self)

    def add_parent(self, parent):
        self.parent.append(parent)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        roots = set()
        courses = dict()
        for i in range(numCourses):
            node = Node(i)
            roots.add(node)
            courses[i] = node

        for d, s in prerequisites:
            courses[s].add_child(courses[d])
            roots.discard(courses[d])

        seen = set()

        def dfs(node):

            for p in node.parent:
                if p.value not in seen:
                    # print("Skipping", node.value, "missing parent", p.value)
                    return
            
            # print("adding", node.value)
            seen.add(node.value)
            for n in node.children:
                dfs(n)


        for node in roots:
            dfs(node)
        
        print(len(seen))
        return len(seen) == numCourses
            
       
        