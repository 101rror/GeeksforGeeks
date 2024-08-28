from collections import defaultdict

class Solution:
    def sortByFreq(self,arr):
        mp = defaultdict(int)
        
        for i in arr:
            mp[i] += 1
        
        ans = sorted(arr, key=lambda x: (-mp[x], x))
            
        return ans



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

        arr = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(arr)
        print(*l)

# } Driver Code Ends