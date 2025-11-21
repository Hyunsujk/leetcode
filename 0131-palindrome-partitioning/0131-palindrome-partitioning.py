class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, slate):
            if start == len(s):
                res.append(slate[:])
                return
            
            for end in range(start, len(s)):
                sub = s[start:end+1]
                if sub == sub[::-1]:
                    slate.append(sub)
                    dfs(end+1, slate)
                    slate.pop()
        dfs(0, [])
        return res