class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        if not queries or len(queries) == 1:
            return [0]
        
        answer = [0] * len(queries)
        colors = [0] * n

        for i, queries in enumerate(queries):
            colorIdx = queries[0]
            color = queries[1]
            oldColor = colors[colorIdx]
            colors[colorIdx] = color

            left = colorIdx - 1
            right = colorIdx +1
            a = answer[i-1] if i >= 1 else 0
            if left >= 0:
                if oldColor != 0 and colors[left] == oldColor:
                    a -= 1
                if colors[left] == color:
                    a += 1
            if right < n:
                if oldColor != 0 and colors[right] == oldColor:
                    a -= 1
                if colors[right] == color:
                    a += 1
            answer[i] = a
        
        return answer

        