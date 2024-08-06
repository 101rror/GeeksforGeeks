#User function Template for python3
class Solution:
    def isValid(self, str):
        ans = str.split('.')
        
        if len(ans) != 4:
            return False
            
        
        for x in ans:
            if x and ((len(x) > 1 and x[0] != '0') or len(x) == 1 ):
                if not (int(x) >= 0 and int(x) <= 255):
                    return False
            else:
                return False
                
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends