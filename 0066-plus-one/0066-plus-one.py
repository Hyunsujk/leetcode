class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        
        place = 10 ** (len(digits)-1)
        for d in digits:
            number += d * place
            place //=10
        
        number += 1
        res = deque()
        while number:
            digit = number % 10
            res.appendleft(digit)
            number //= 10
        
        return list(res)
