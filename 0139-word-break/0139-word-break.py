class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        word_lengths = set([len(w) for w in wordDict])
        n = len(s)

        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for l in word_lengths:
                if l <= i and dp[i-l] and s[i-l:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]