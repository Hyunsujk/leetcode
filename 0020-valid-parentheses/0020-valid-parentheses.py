class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for b in s:
            if b not in pair:
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                o = stack.pop()
                if o != pair[b]:
                    return False
        
        return len(stack) == 0