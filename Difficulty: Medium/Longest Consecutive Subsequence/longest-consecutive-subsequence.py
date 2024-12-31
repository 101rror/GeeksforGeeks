 #User function Template for python3
from collections import Counter

class Solution:
    def longestConsecutive(self,arr):
        arrset = set(arr)
        maxlen = 0
        
        for num in arrset:
            if num - 1 not in arrset:
                cur = num
                count = 1
                
                while cur + 1 in arrset:
                    cur += 1
                    count += 1
                    
                maxlen = max(maxlen, count)
                
        return maxlen
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
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends