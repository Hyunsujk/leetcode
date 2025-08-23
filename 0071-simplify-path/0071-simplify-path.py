class Solution:
    def simplifyPath(self, path: str) -> str:
        if path[0] != "/":
            return ""
        left = 0
        right = 1
        p = []

        while right <= len(path):
            if right < len(path) and path[right] != "/":
                right += 1
            else:
                word = path[left+1:right]
                if word == "..":
                    if p:
                        p.pop()
                elif word != "." and word != "":
                    p.append(word)
                left = right
                right += 1
        
        return "/" + "/".join(p)

        