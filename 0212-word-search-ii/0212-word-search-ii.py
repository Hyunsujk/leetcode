class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsT = Trie()

        for word in words:
            wordsT.add(word)
        
        rows = len(board)
        cols = len(board[0])
        found = set()

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return

            node = node.children[char]
            if node.end_word:
                found.add(node.end_word)

            temp, board[r][c] = board[r][c], '#'

            for rowDiff, colDiff in [(1,0), (-1,0), (0,1), (0,-1)]:
                newRow = r + rowDiff
                newCol = c + colDiff
                if 0 <= newRow < rows and 0 <= newCol < cols and board[newRow][newCol] != '#':
                    dfs(newRow, newCol, node)

            board[r][c] = temp 

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, wordsT.root)
        
        return list(found)

        