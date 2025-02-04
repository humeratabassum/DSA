#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        left_r=s1[2:]+s1[:2]
        right_r=s1[-2:]+s1[:-2]
        
        return s2==left_r or s2==right_r
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        p = str(input())
        if (Solution().isRotated(s, p)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends