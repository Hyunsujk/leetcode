class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def match(self, word, reverse = False):
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

        seen = defaultdict(int)
        count = 0
        for word in words:
            prefixes = prefixT.match(word)
            reverseW = word[::-1]
            suffixes = suffixT.match(reverseW, True)
            for p in prefixes:
                if p in suffixes:
                    count += seen[p]
            seen[word] += 1
        
        return count


        