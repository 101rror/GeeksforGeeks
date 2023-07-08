#User function Template for python3


class Solution:
    def findTriplets(self, arr, n):
        if(n < 3):
            return 0
        else:
            arr = sorted(arr)
            
            for i in range(n):
                left = i + 1
                right = n - 1
                
                while(left < right):
                    summ = (arr[i] + arr[left] + arr[right])
                    
                    if(summ == 0):
                        return 1
                    elif(summ < 0):
                        left += 1
                    else:
                        right -= 1
        return 0

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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends