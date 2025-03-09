#User function Template for python3

class Solution:
    def countPS(self, s):
        n = len(s)
        ans = 0
        
        for i in range(n):
            for h in (i, i + 1):
                l = i - 1
                while l >= 0 and h < n and s[l] == s[h]:
                    l -= 1
                    h += 1
                    ans += 1
                    
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends