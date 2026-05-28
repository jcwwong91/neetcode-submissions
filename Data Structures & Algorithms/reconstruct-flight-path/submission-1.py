class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        destinations = dict()
        tickets.sort()

        for ticket in tickets:
            src = ticket[0]
            dst = ticket[1]
            if src not in destinations:
                destinations[src] = list()
            destinations[src].append(dst)
        
        ret = ["JFK"]
        def dfs(src):
            if len(ret) == len(tickets) + 1:
                return True
            if src not in destinations:
                return False

            length = len(destinations[src])
            for i in range(length):
                v = destinations[src][i]
                ret.append(v)
                destinations[src].pop(i)
                if dfs(v):
                    return True
                destinations[src].insert(i, v)
                ret.pop()

        dfs(ret[0])
            

        return ret
        