# optimal solution using bit manipukatiom
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&(n-1)==0)








#bruteforce approach
"""
        if n<=0:
            return False
        while n!=1:
            if n%2!=0:
                return False
            n=n//2
        return True
"""