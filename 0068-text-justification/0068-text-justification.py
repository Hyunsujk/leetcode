class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        def helper(i, line, length):
            if i == len(words):
                subline = " ".join(line)
                subline += " " * (maxWidth - len(subline))
                res.append(subline)
                return
            currW = words[i]
            totalSpaces = maxWidth - length
            if length + len(line) + len(currW) > maxWidth:
                spaceSections = len(line)-1
                if spaceSections == 0:
                    subline = line[0]
                    subline += " " * totalSpaces
                else:
                    even, extra = divmod(totalSpaces, spaceSections)
                    subline = ""
                    for j in range(spaceSections):
                        subline += line[j] + " " * (even + (1 if j < extra else 0))
                    subline += line[-1]
                res.append(subline)
                return helper(i+1, [currW], len(currW))
            else:
                line.append(currW)
                return helper(i+1, line, length + len(currW))
        
        helper(0, [], 0)
        return res

        