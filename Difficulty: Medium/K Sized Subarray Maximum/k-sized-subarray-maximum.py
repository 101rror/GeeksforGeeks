#User function Template for python3

class Solution:
    def max_of_subarrays(self,k,arr):
        n = len(arr)
        ans = []
        
        cur = max(arr[:k])
        ans.append(cur)
        
        for i in range(1, n - k + 1):
            if arr[i - 1] == cur:
                cur = max(arr[i : i + k])
            else:
                cur = max(cur, arr[i + k - 1])
            
            
            ans.append(cur)
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.max_of_subarrays(k, arr)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends