class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        seen_count = defaultdict(int)
        seen_count[words[0]] = 1
        seen_lengths = set([len(words[0])])
        
        total = 0

        for i in range(1, len(words)):
            word = words[i]
            curr_length = len(word)
            for prev in seen_lengths:
                if prev > curr_length:
                    continue
                elif prev == curr_length:
                    total += seen_count[word]
                else:
                    prefix = word[:prev]
                    if prefix == word[curr_length-prev:]:
                        total += seen_count[prefix]
            seen_count[word] += 1
            seen_lengths.add(curr_length)

        return total
        