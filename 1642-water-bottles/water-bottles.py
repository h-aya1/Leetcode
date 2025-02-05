class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        while numBottles >= numExchange:
            newB = numBottles // numExchange
            drunk += newB 
            numBottles = newB + (numBottles % numExchange)
        return drunk