class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank=numBottles
        empty=numBottles

        while empty>=numExchange:
            full=empty//numExchange
            drank+=full
            empty=empty%numExchange+full
        return drank


        