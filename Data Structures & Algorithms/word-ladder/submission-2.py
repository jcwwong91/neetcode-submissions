
from string import ascii_lowercase

class Node:
    def __init__(self, word):
        self.value = word
        self.neighbors = set()

    def set_neighbor(self, neighbor, first=True):
        self.neighbors.add(neighbor)



class Solution:

    def loadWords(self, wordList):
        self.words = dict()
        for word in wordList:
            self.words[word] = Node(word)

        for word in wordList:
            for i in range(len(word)):
                for c in ascii_lowercase:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word == word:
                        continue
                    if new_word in self.words:
                        self.words[word].set_neighbor(new_word)
                        self.words[new_word].set_neighbor(word)


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        self.loadWords(wordList)
        
        if endWord not in self.words:
            return 0

        
        def bfs(nodes, seen, level):

            queue = set()
            # print(nodes)
            for n in nodes:
                print(n)
                node = self.words[n]
                if node.value in seen:
                    continue
                if node.value == endWord:
                    return level
                seen.add(node.value)
                # print(node.value, node.neighbors)
                for neighbor in node.neighbors:
                    if neighbor in seen:
                        continue
                    queue.add(neighbor)

            # print(queue)
            if len(queue) == 0:
                return 0
            
            return bfs(list(queue), seen, level+1)

        
        if beginWord in self.words:
            return bfs([beginWord], set(), 1)

        words = set()
        for i in range(len(beginWord)):
            for c in ascii_lowercase:
                word = beginWord[:i] + c + beginWord[i+1:]
                if beginWord == word:
                    continue
                if word in self.words:
                    words.add(word)
        return bfs(list(words), set(), 2)
