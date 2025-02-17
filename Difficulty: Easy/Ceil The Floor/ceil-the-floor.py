
class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        floor, ceil = -1, -1  # Correct variable name for ceil

        for num in arr:
            if num <= x:
                floor = max(floor, num)
            if num >= x:
                ceil = min(ceil if ceil != -1 else float('inf'), num)  # Fixed 'ceil' typo
        
        return [floor, ceil]  # Fixed return statement

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends