class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        seen_count = defaultdict(int)
        seen_count[words[0]] = 1
        seen_length = set([len(words[0])])

        total = 0

        for i in range(1,len(words)):
            word = words[i]
            curr_l = len(word)

            for prev_l in seen_length:
                if prev_l > curr_l:
                    continue
                elif prev_l == curr_l:
                    total += seen_count[word]
                else:
                    prefix = word[:prev_l]
                    if prefix == word[curr_l - prev_l:]:
                        total += seen_count[prefix]
            seen_length.add(curr_l)    
            seen_count[word] += 1       

        
        return total

        