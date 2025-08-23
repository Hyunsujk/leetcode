class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for n in arr1:
            while n:
                prefixes.add(n)
                n //= 10
        
        prefix = 0
        for n in set(arr2):
            while n:
                if n in prefixes:
                    prefix = max(prefix, n)
                n //= 10
        
        return len(str(prefix)) if prefix != 0 else prefix
        