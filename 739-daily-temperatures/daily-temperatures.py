class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        nextWarm = defaultdict(int)
        ans = []


        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                lestemp = stack.pop()
                nextWarm[lestemp] = i

            stack.append(i)

        for idx in range(len(temperatures)):

            ans.append(max(0, nextWarm[idx] - idx))

        
            
        

        return ans