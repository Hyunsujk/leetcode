class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        found = []

        trie = Trie()

        for word in words:
            trie.add(word)
        
        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                found.append(next_node.word)
                next_node.word = ""
            
            board[r][c] = "#"

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

            board[r][c] = char

            if not next_node.children and not next_node.word:
                node.children.pop(char)
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return found