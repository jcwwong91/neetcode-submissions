class Node:
    def __init__(self, value):
        self.value = value
        self.children = dict()
        self.endable = False

    def get_children(self, key):
        if key == '.':
            return list(self.children.values())
        
        return [self.children.get(key)] if key in self.children else []

    def set_child(self, key):

        if key not in self.children:
            self.children[key] = Node(key)

        return self.children[key]

    def is_endable(self):
        return self.endable

    def set_endable(self):
        self.endable = True



class WordDictionary:

    def __init__(self):
        self.root = Node("")
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.set_child(c)

        # print("ending at", node.value, node)
        node.set_endable()

    def search(self, word: str) -> bool:
        
        def traverse(node, word, baseword=None) -> bool:
            if word == "":
                # print("triggered", node.value, node.endable, baseword, word, node)
                return node.is_endable()

            c = word[0]
            children = node.get_children(c)
            for child in children:
                if traverse(child, word[1:], baseword=baseword):
                    return True
            return False

        return traverse(self.root, word, baseword=word)
        

        
