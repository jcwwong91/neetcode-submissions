class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = dict() # Map the source to dest flgihts
        for flight in flights:
            if flight[0] not in edges:
                edges[flight[0]] = list()
            edges[flight[0]].append((flight[1], flight[2]))

        
        minPrice = {src: 0}
        cities = [src]
        for i in range(k + 1):
            visited = set()
            # print("iteration", i, cities)
            curPrice = dict()
            for sc in cities:
                for dc, cost in edges.get(sc, []):
                    # print("s:", sc,"d:", dc, "new:",  minPrice[sc] + cost, "(", minPrice[sc], cost, ")", "exist:", minPrice.get(dc))
                    curPrice[dc] = min(minPrice[sc] + cost, curPrice.get(dc, minPrice[sc] + cost))
                    visited.add(dc)
            cities = list(visited)
            for k,v in curPrice.items():
                minPrice[k] = min(v, minPrice.get(k, v))
            # print("costs", minPrice)

        return minPrice.get(dst, -1)

        
