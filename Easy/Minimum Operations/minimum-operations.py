#User function Template for python3

class Solution:
    def minOperation(self, n):
        count = 0
        
        while n != 0:
            if n % 2 == 0:
                n = n / 2
            elif n % 2 != 0:
                n = n - 1
            count += 1
            
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends