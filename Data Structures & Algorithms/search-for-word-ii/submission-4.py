class Node:
    def __init__(self):
        self.children = dict()
        self.word = None
    
    def set_word(self, word):
        self.word = word

    def exist(self, word, p):
        if self.word == word:
            return True
        
        if p == len(word):
            return False
        
        child = self.children.get(word[p])
        if not child:
            return False
        
        child.exist(word, p+1)



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.build_trie(words)
        
        queue = list()
        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if c in root.children:
                    queue.append((i, j, root.children[c]))
        

        ret = set()
        def traverse(i, j, node, seen):
            # print("traversing", i, j, node, seen)
            if node.word:
                # print("setting", i, j, node)
                ret.add(node.word)

            if len(node.children) == 0:
                return

            for ii, jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if ii < 0 or ii >= len(board) or jj < 0 or jj >= len(board[0]) or (ii, jj) in seen:
                    continue
                
                # print(ii,jj,seen)
                c = board[ii][jj]
                if c in node.children:
                    seen.add((ii,jj))
                    traverse(ii,jj,node.children[c],seen)
                    seen.remove((ii,jj))
            
                
        for (i, j, node) in queue:
            traverse(i, j, node, {(i,j)})

        return list(ret)

    
    def build_trie(self, words):

        root = Node()

        for w in words:
            node = root
            for c in w:
                child = node.children.get(c)
                if not child:
                    child = Node()
                    node.children[c] = child
                node = child
            node.set_word(w)
            # print(node)
        
        return root



        