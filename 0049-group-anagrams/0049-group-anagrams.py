class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        if len(strs) == 1:
            return [[strs[0]]]

        for s in strs:
            chars = str(sorted([c for c in s]))
            if chars not in group:
                group[chars] = []
            group[chars].append(s)
        
        return list(group.values())