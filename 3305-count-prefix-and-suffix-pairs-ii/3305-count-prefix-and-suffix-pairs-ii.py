class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def match(self, word: str, reverse = False):
        node = self.root
        matches = set()

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
        total = 0

        count = defaultdict(int)
        
        for word in words:
            prefixes = prefixT.match(word)
            reversedw = word[::-1]
            suffixes = suffixT.match(reversedw, True)
            for p in prefixes:
                if p in suffixes:
                    total += count[p]
            count[word] += 1
            
        return total


        