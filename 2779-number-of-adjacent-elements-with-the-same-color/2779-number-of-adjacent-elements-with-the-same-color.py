class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        if not queries and len(queries) == 1:
            return [0]

        answer = []
        colors = [0] * n
        adjacent = 0

        for i, color in queries:
            c = colors[i]
            if c != 0:
                if i-1 >= 0 and colors[i-1] == c:
                    adjacent -= 1
                if i+1 < n and colors[i+1] == c:
                    adjacent -= 1
            
            colors[i] = color

    
            if i-1 >= 0 and colors[i-1] == color:
                adjacent += 1
            if i+1 < n and colors[i+1] == color:
                adjacent += 1
            answer.append(adjacent)
        
        return answer
        