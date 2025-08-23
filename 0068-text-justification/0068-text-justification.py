class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        def helper(i, line, length):
            if i == len(words):
                subline = " ".join(line)
                subline += " " * (maxWidth - len(subline))
                res.append(subline)
                return

            currWord = words[i]
            if length + len(line) + len(currWord) > maxWidth:
                spaceSection = len(line)-1
                spaces = maxWidth - length
                if spaceSection == 0:
                    subline = line[0] + " " * spaces
                else:
                    evenSpaces, extraSpaces = divmod(spaces, spaceSection)
                    subline = ""
                    for j in range(spaceSection):
                        subline += line[j] + " " * (evenSpaces + (1 if j < extraSpaces else 0))
                    subline += line[-1]
                res.append(subline)
                return helper(i+1, [currWord], len(currWord))
            else:
                line.append(currWord)
                return helper(i+1, line, length + len(currWord))
            
        helper(0, [], 0)
        return res
        