#User function Template for python3


class Solution:
    def nextHappy (self, n):
        def isHappy(n):
            seen = set()
            
            while (n not in seen):
                seen.add(n)
                n = sum([int(x) ** 2 for x in str(n)])
                
            return (n == 1)
        
        n += 1
        while (not isHappy(n)):
            n += 1
        
        return n

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends