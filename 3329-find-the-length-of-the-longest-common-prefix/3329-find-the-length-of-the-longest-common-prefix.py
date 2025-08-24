class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        
        for a in arr1:
            while a:
                prefixes.add(a)
                a //= 10
        
        maxP = 0
        for a in arr2:
            while a:
                if a in prefixes:
                    maxP = max(maxP, a)
                a //= 10
        
        return len(str(maxP)) if maxP != 0 else 0


        