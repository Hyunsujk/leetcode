class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        def helper(i, length, line):
            if i == len(words):
                line_str = " ".join(line)
                line_str += " " * (maxWidth - len(line_str))
                res.append(line_str)
                return

            spaces = len(line)
            if length + spaces + len(words[i]) > maxWidth:
                space_count = len(line) - 1
                if space_count == 0:
                    line_str = line[0] + " " * (maxWidth - len(line[0]))
                    res.append(line_str)
                else:
                    total_space = maxWidth - sum(len(w) for w in line)
                    even_space, extra_space = divmod(total_space, space_count)
                    line_str = ""
                    for j in range(space_count):
                        line_str += line[j] + (" " * (even_space + (1 if j < extra_space else 0)))
                    line_str += line[-1]
                    res.append(line_str)

                return helper(i+1, len(words[i]), [words[i]])
            else:
                line.append(words[i])
                return helper(i+1, length + len(words[i]), line)
        
        helper(0, 0, [])
        return res