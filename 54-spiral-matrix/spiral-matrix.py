class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []

        top = 0
        bot = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1

        while top <= bot and l <= r:

            for i in range(l, r + 1):
                ans.append(matrix[top][i])
            top += 1  

            for i in range(top, bot + 1):
                ans.append(matrix[i][r])
            r -= 1  

            if top <= bot:
                for i in range(r, l - 1, -1):
                    ans.append(matrix[bot][i])
                bot -= 1             
            
            if l <= r:
                for i in range(bot, top - 1, -1):
                    ans.append(matrix[i][l])
                l += 1  
                
        return ans