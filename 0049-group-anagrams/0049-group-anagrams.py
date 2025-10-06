class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        if len(strs) == 1:
            return [[strs[0]]]

        for s in strs:
            chars = "".join(sorted(s))
            group[chars].append(s)
        
        return list(group.values())