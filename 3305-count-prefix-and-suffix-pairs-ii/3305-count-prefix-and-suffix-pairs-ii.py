class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        seen_count = defaultdict(int)
        seen_count[words[0]] = 1
        prev_lengths = set([len(words[0])])

        total = 0

        for i in range(1, len(words)):
            word = words[i]
            curr_length = len(word)

            for prev_length in prev_lengths:
                if prev_length > curr_length:
                    continue
                elif prev_length == curr_length:
                    total += seen_count[word]
                else:
                    prefix = word[:prev_length]
                    if prefix == word[curr_length - prev_length:]:
                        total += seen_count[prefix]
            prev_lengths.add(curr_length)
            seen_count[word] += 1
        return total
                    
