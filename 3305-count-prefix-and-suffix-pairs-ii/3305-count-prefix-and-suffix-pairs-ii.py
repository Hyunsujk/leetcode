class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def match(self, word, reverse = False):
        matches = set()
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if node.end_word:
                matches.add(node.end_word)
        node.end_word = word[::-1] if reverse else word
        
        return matches

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        prefixT = Trie()
        suffixT = Trie()

        seen = defaultdict(int)
        total = 0
        for w in words:
            prefixes = prefixT.match(w)
            reversedW = w[::-1]
            suffixes = suffixT.match(reversedW, True)
            for p in prefixes:
                if p in suffixes:
                    total += seen[p]
            seen[w] += 1            
        
        return total
        