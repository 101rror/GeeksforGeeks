#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        ans = [0] * n
        st = set()
        
        for i in range(1, n):
            ans[i] = ans[i - 1] - i
            
            if(ans[i] <= 0 or ans[i] in st):
                ans[i] = ans[i - 1] + i
            
            st.add(ans[i])
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends