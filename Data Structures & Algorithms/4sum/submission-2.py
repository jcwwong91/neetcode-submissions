class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # print(nums)
        ret = set()
        for i in range(len(nums)-2):    
            a = nums[i]
            for j in range(i+1, len(nums)-1, 1):
                b = nums[j]
                t = target - a - b
                l = j+1
                r = len(nums)-1
                # print(f'handling: {a}({i}),{b}({j}) - {t}')
                while l < r:
                    c = nums[l]
                    d = nums[r]
                    # print(f'lr: {c}({l}) {d}({r}),   {c + d}')
                    res = c + d
                    if res == t:
                        # print(f'{a}({i}),{b}({j}),{c}({l}),{d}({r})')
                        ret.add((a,b,c,d))
                        l += 1
                        r -= 1
                        continue
                    if res < t:
                        l +=1
                        continue
                    r -= 1
        return list(ret)
