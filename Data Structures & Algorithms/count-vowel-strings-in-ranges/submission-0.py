class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = {'a', 'e','i','o','u'}
        ret = list()
        for (start, end) in queries:
            count = 0
            for i in range(start, end+1):
                word = words[i]
                if word[0] in vowels and word[-1] in vowels:
                    count += 1
            ret.append(count)
        return ret