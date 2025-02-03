class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges.sort()
        for ran in ranges:
            if ran[0] <= left <= ran[1]:
                left = ran[1] + 1
            if left > right:
                return True

        return left > right