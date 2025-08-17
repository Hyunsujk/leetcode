class TrieNode:
    def __init__(self):
        self.children = {}
        self.ending_word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def matches(self, word, reverse = False):
        matches = set()
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
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

        for word in words:
            prefixes = prefixT.matches(word)
            reversedWord = word[::-1]
            suffixes = suffixT.matches(reversedWord, True)
            for p in prefixes:
                if p in suffixes:
                    total += count[p]
            count[word] += 1
        
        return total


        