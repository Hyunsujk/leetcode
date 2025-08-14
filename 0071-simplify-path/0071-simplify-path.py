class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path or path[0] != "/":
            return ""
        
        l = 1
        r = 1
        n = len(path)

        simplified = []

        while r <= n:
            if r == n or path[r] == "/":
                subPath = path[l:r]
                if subPath == "..":
                    if simplified:
                        simplified.pop()
                elif subPath and subPath != ".":
                    simplified.append(subPath)
                r += 1
                l = r
            else:
                r += 1
    
        return "/" + "/".join(simplified)
