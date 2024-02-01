from collections import defaultdict 

class Solution:
    def checkPangram(self,s):
        s = s.lower()
        st = set()
        
        for i in s:
            if(ord(i) >= ord("a") and ord(i) <= ord("z")):
                st.add(i)
            
        if(len(st) == 26):
            return True
        return False

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
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends