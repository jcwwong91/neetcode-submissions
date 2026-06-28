class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        largest = max(weights)

        def days_to_ship(ship):

            cur = 0
            days = 0
            for w in weights:
                cur += w
                if cur > ship:
                    days += 1
                    cur = w
            
            return days + 1

        
        ret = 0
        l = largest
        r = total
        while l <= r:
            m = l + ((r - l) // 2)
            d = days_to_ship(m)
            # print(l, m, r, d)
            if d <= days:
                ret = m
            if d > days:
                l = m + 1
            else:
                r = m - 1
        return ret