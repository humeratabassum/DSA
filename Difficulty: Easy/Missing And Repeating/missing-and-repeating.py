#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        n=len(arr)
        freq=[0]*(n+1)
        
        for num in arr:
            freq[num]+=1 #count array freq
        m,r=-1,-1
        for i in range(1,n+1):
            if freq[i]>1:
                r=i
            elif freq[i]==0:
                m=i
        return [r,m]
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends