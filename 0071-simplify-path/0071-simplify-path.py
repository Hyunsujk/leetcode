class Solution:
    def simplifyPath(self, path: str) -> str:
        left = 0
        right = 1
        stack = []
        while right < len(path):
            while right < len(path) and path[right] != "/":
                right += 1
            
            if right - left > 1:
                p = path[left+1:right]
                if p == "..":
                    if stack:
                        stack.pop()
                elif p != ".":
                    stack.append(p)
            
            left = right
            right += 1

        
        
        return "/" + "/".join(stack)
               