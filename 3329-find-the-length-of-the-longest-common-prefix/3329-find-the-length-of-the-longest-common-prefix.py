class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_prefix = set(arr1)

        for n in arr1:
            base = 10
            while n:
                n = n // base
                arr1_prefix.add(n)
            
        longest_prefix = 0
        for n in set(arr2):
            if n in arr1_prefix:
                longest_prefix = max(longest_prefix, n)
            while n:
                n = n // 10
                if n in arr1_prefix:
                    longest_prefix = max(longest_prefix, n)

        
        return len(str(longest_prefix)) if longest_prefix != 0 else 0


        