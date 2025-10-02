class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty= numBottles

        while empty>=numExchange:
            full=1
            empty-=numExchange
            total+=full
            empty+=full
            numExchange+=1
        return total

        