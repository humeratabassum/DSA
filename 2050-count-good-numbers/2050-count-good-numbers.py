class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=(10**9)+7

        even= (n+1)//2
        odd=n//2

        # total cominations : (5 ^ even positions ×4^ odd positions)%(10^9 +7)

        total_combinations=(pow(5,even,mod)*pow(4,odd,mod))%mod
        return total_combinations

        