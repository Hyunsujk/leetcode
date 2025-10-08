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
                if not stack or stack.pop() != pair[b]:
                    return False
        
        return len(stack) == 0