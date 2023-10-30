#User function Template for python3

import math

class Solution:
    def sumXOR (self, arr, n) : 
        tsum = 0
        
        high = int(math.log2(max(arr)) + 1)
        
        for i in range(high):
            x = 0
            
            for j in arr:
                if (j & (1 << i)):
                    x += 1
            tsum += (x * (n - x) * (1 << i))
            
        return tsum



#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends