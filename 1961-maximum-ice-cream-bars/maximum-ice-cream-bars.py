class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if min(costs) > coins:
            return 0
        if sum(costs) < coins:
            return len(costs)
            
        idx = [0]*(max(costs)+1)
        for i in costs:
            idx[i] += 1
       

        ans = [0] * len(costs)
        j = 0
        for i in range(len(idx)):
            if idx[i] != 0:
                
                while idx[i] != 0:
                    ans[j] = i
                    idx[i] -= 1
                    j += 1
            else:
                continue
        print(ans)
        tot = 0
        i = 0
        while i < len(ans) and tot <= coins:
            tot += ans[i]
            i += 1
        return i - 1
        