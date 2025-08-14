class Solution:
    def simplifyPath(self, path: str) -> str:
        subPaths = path.split("/")
        simplified = []

        for p in subPaths:
            if p == "..":
                if simplified:
                    simplified.pop()
            elif p == "." or p == "":
                continue
            else:
                simplified.append(p)
        
        return "/" + "/".join(simplified)