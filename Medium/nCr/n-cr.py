#User function Template for python3

class Solution:
    def nCr(self, n, r):
        
        def findfactorial(num):
            ans = 1
            
            for i in range(1, num + 1):
                ans *= i
                
            return ans
            
                
        mod = 10**9+7
        x = (n - r)
        
        t1 = findfactorial(n)
        t2 = findfactorial(r)
        t3 = findfactorial(x)
        
        res = int(t1 // (t2 * t3))
        
        ans = int(res % mod)
        
        return int(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends