class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []
        for b in s:
            if b not in brackets:
                stack.append(b)
            else:
                if not stack or brackets[b] != stack.pop():
                    return False
        
        return len(stack) == 0
