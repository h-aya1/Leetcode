class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            num = str(num)
            for d in num:
                ans.append(int(d))
        return ans

