class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, slate):
            if start == len(s) and slate:
                res.append(slate[:])

            for end in range(start, len(s)):
                sub_str = s[start: end+1]
                if sub_str == sub_str[::-1]:
                    slate.append(sub_str)
                    dfs(end+1, slate)
                    slate.pop()
        
        dfs(0, [])
        return res