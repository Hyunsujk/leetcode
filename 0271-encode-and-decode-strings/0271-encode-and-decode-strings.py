class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        start = 0
        end = 0
        while end < len(s):
            if s[end] != "#":
                end += 1
            else:
                length = int(s[start:end])
                word = s[end+1:end+1+length]
                res.append(word)
                start = end+1+length
                end = start
        
        return res



        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))