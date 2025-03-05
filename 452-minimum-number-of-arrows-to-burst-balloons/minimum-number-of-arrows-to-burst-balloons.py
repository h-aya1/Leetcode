class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=
        lambda x: x[1])
        
        burst = float('-inf')
        count = 0

        for start , end in points:

            if start > burst:

                burst = end
                count += 1

        return count

