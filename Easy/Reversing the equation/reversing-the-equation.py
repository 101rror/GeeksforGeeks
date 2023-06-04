#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        c = []
        o = []
        n = ''
        
        for x in s:
            if (x not in "+-/*"):
                n += x
                
            else:
                c.append(n)
                n =''
                o.append(x)
                
        c.append(n)
        ans = ''
        
        while c:
            ans += c.pop()
            
            if o:
                ans += o.pop()
                
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends