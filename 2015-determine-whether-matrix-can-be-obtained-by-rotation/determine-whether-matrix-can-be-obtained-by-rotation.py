class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        for _ in range(4):  
            
            if mat == target:
                return True

            new_mat = []
            for j in range(n):  
                row = []
                for i in range(n - 1, -1, -1):
                    row.append(mat[i][j])
                new_mat.append(row)
            
            mat = new_mat 
        return False
