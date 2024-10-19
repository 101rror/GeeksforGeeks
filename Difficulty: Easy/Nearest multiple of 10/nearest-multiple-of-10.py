#User function Template for python3
import sys

sys.set_int_max_str_digits(10 ** 5 + 1)

class Solution:
    def roundToNearest (self, s) : 
        ints = int(s) + 4
        
        div = (ints // 10) * 10
        new = str(div)
        
        return new.zfill(len(s))


#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends