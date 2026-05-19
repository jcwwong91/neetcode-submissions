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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        roots = set()
        courses = dict()
        for n in range(numCourses):
            node = Node(n)
            roots.add(node)
            courses[n] = node
        for d, s in prerequisites:
            roots.discard(courses[d])
            courses[s].add_child(courses[d])

        ret = list()
        visited = set()
        
        def dfs(node):

            for p in node.parent:
                if p not in visited:
                    # print("cannot handle", node.value, "due to missing", p.value)
                    return

            ret.append(node.value)
            visited.add(node)
            #print("adding", node.value)

            for c in node.children:
                dfs(c)

        for node in roots:
            #print("p", node.value)
            dfs(node)

        if len(ret) != numCourses:
            return []
        return ret
        