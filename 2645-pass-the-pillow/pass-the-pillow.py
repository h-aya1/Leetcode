class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full = time // (n - 1)
        extra = time % (n - 1)
        if full % 2 == 0 :
            return extra + 1
        return n - extra