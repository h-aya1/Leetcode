class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        result = []
        
        for _ in range(cols):  
            result.append([0] * rows) 

        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        
        return result