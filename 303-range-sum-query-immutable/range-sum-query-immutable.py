class NumArray:

    def __init__(self, nums: List[int]):

        self.nums = nums

        self.preSum = []
        sums = 0
        for i in range(len(self.nums)):
            sums += self.nums[i] 
            self.preSum.append(sums)

    def sumRange(self, left: int, right: int) -> int:
        
        if left == 0:
            return self.preSum[right]
        else:
            return self.preSum[right] - self.preSum[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)