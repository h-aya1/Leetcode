class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans = [0]*2
        nums.sort()
        nums = Counter(nums)
        for val , freq in nums.items():
            if freq % 2 == 0:
                ans[0]  += (freq // 2)
            elif  freq % 2 != 0 and freq > 2:
                ans[0] += (freq // 2)
                ans[1] += 1
            else:
                ans[1] += 1
        return ans