class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = Counter(answers)
        rab = 0

        for n in ans:
            group_size = n + 1  
            groups = (ans[n] + group_size - 1) // group_size  
            rab += groups * group_size

        return rab