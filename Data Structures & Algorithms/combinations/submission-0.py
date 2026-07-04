class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ret = list()
        def combine(cur, i, count):
            nonlocal ret
            # print(cur, i ,count)
            if count == 1:
                for j in range(i, n+1):
                    # print(cur, j)
                    ret.append(cur + [j])
                return
            
            # print("iterate", i, n+2-count)
            for j in range(i, n + 2 - count):
                new_cur = cur + [j]
                # print("new", new_cur, j+1, count-1)
                combine(new_cur, j + 1, count - 1)

        combine(list(), 1, k)
        return ret