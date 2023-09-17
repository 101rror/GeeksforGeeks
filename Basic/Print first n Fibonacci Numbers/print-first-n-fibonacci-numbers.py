#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self, n):
        ans = []
        one = []
        one.append(1)
        
        ans.append(1)
        ans.append(1)
        
        if(n == 1):
            return one
        if(n == 2):
            return ans
        
        for i in range(1, n - 1):
            x = ans[i] + ans[i - 1]
            ans.append(x)
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends