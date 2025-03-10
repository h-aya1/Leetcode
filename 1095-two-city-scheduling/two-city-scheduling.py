class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x : x[0] - x[1] )

        mid = len(costs) // 2

        ans = 0

        for i in range(mid):
            ans += costs[i][0]

            
        for j in range(mid,len(costs)):
            ans += costs[j][1]
        

        return ans