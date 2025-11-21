class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(start, st, slate):
            if start == len(s) and slate:
                res.append(slate[:])
                return

            for end in range(start, len(s)):
                substring = s[start:end+1]
                if self.is_palin(substring):
                    slate.append(substring)
                    helper(end+1, substring, slate)
                    slate.pop()

        helper(0, "", [])
        return res
    
    def is_palin(self, s):
        return s == s[::-1]

