class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = {'a', 'e','i','o','u'}
        prefix = [0] * (len(words) + 1)
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                prefix[i+1] = prefix[i] + 1
            else:
                prefix[i+1] = prefix[i]
        ret = list()
        for (s, e) in queries:
            ret.append(prefix[e+1] - prefix[s])

        return ret
