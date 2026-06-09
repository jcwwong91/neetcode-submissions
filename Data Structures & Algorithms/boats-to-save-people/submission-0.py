class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l = 0
        r = len(people) - 1
        print(people)
        while l < r:
            if people[l] + people[r] <= limit:
                # print(f'{people[l]}({l}), {people[r]}({r})')
                l += 1
                r -= 1
            else:
                # print(f'{people[r]}({r})')
                r -= 1
                
            boats += 1
        if l == r:
            boats += 1
        
        return boats