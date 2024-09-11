#User function Template for python3

from heapq import*

class Solution:
   def minCost(self, arr):
        n = len(arr)
        ans = 0
        minheap = []
        
        for i in range(len(arr)):
            heappush(minheap, arr[i])
            
        while len(minheap) >= 2:
            a = heappop(minheap)
            b = heappop(minheap)
            ans += (a + b)
            heappush(minheap,(a + b))
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import defaultdict
# Contributed by : Nagendra Jha

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
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))

# } Driver Code Ends