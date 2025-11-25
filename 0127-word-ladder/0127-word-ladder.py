class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        L = len(beginWord)
        patterns = defaultdict(list)

        for word in wordList:
            for i in range(L):
                key = word[:i] + "*" + word[i+1:]
                patterns[key].append(word)
        
 
        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while q:
            w, level = q.popleft()
            if w == endWord:
                return level

            for i in range(L):
                key = w[:i] + "*" + w[i+1:]
                for candidate in patterns[key]:
                    if candidate not in visited:
                        q.append((candidate, level+1))
                        visited.add(candidate)
        
        return 0
        
 
