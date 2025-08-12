class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_prefix = set()

        for n in arr1:
            while n:
                arr1_prefix.add(n)
                n = n // 10
        
        longest_prefix_len = 0
        for n in set(arr2):
            while n:
                if n in arr1_prefix:
                    longest_prefix_len = max(longest_prefix_len, len(str(n)))
                    break
                n = n // 10
        
        return longest_prefix_len
        