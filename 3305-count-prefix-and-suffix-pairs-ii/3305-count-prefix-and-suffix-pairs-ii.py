class TrieNode:
    def __init__(self):
        self.children = {}
        self.ending_word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str, reverse = False):
        node = self.root

        matches = set()
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode()
                node.children[char] = new_node
                node = new_node
            if node.ending_word:
                matches.add(node.ending_word)
        node.ending_word = word[::-1] if reverse else word
        return matches
    


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        prefixT = Trie()
        suffixT = Trie()
        
        count = defaultdict(int)
        total = 0
        for w in words:
            prefixes = prefixT.add(w)
            rw = w[::-1]
            suffixes = suffixT.add(rw, True)
            for p in prefixes:
                if p in suffixes:
                    total += count[p]
            count[w] += 1
        
        return total

        