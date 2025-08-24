class Solution:
    def simplifyPath(self, path: str) -> str:
        left = 0
        right = 1

        simplified = []

        while right <= len(path):
            if right < len(path) and path[right] != "/":
                right += 1
            else:
                p = path[left+1:right]
                if p == "..":
                    if simplified:
                        simplified.pop()
                elif p != "." and p != "":
                    simplified.append(p)
                left = right
                right += 1
        
        return "/" + "/".join(simplified)
                        
        