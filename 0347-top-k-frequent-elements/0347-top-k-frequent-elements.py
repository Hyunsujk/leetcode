class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        freql = [(num, f) for num, f in freq.items()]
        freql.sort(key = lambda x:x[1], reverse=True)

        l = []
        for i in range(k):
            l.append(freql[i][0])
        
        return l



        