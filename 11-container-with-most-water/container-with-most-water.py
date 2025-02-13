class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_a = 0
        
        while i < j:
            w = j - i
            curr_h = min(height[i], height[j])
            area = w * curr_h
            max_a = max(max_a, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_a
