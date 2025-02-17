class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        l,r=0,len(arr)-1
        floor=-1
        
        
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]<k:
                floor=mid
                l=mid+1
            else:
                r=mid-1
        return floor
            
        #Your code here
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends