#User function Template for python3

class Solution:
    def colName (self, n):
        char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        ans = ""
        
        while(n):
            rem = n % 26
            
            if(rem == 0):
                n -= 1
            
            ans += char[rem - 1]
            
            n //= 26
            
        return ans[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends