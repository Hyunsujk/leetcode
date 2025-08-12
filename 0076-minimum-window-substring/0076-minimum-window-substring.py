class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tCount = Counter(t)
        window = {}
        res = [-1, -1]
        minLength = float("inf")

        have = 0
        need = len(tCount)

        left = 0

        for right in range(len(s)):
            rchar = s[right]
            if rchar not in window:
                window[rchar] = 0
            window[rchar] += 1

            if rchar in tCount and window[rchar] == tCount[rchar]:
                have += 1

            while have == need:
                if (right - left + 1) < minLength:
                    res = [left, right]
                    minLength = right - left + 1
                
                lchar = s[left]
                window[lchar] -= 1
                if lchar in tCount and window[lchar] < tCount[lchar]:
                    have -= 1
                left += 1
        
        return s[res[0]: res[1]+1] if minLength != float("inf") else ""

