class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        a,b=0,1
        for _ in range(2,n+1):
            a,b=b,a+b
        return b

            # return self.fib(n-1)+self.fib(n-2)





        # n1,n2=0,1
        # for _ in range(2,n+1):
        #     n1,n2=n2,n1+n2
        # return n2

        