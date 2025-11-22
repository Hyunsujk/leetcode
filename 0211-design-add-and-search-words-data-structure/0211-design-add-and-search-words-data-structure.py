class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_end
            if word[i] != ".":
                if word[i] not in node.children:
                    return False
                return dfs(i+1, node.children[word[i]])
            else:
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True
                return False

        return dfs(0, self.trie)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)