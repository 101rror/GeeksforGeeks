#User function Template for python3

class Solution:
    def longestPalin(self, S):
        n = len(S)
        def get(l,h):
            while l >= 0 and h < n:
                if S[l]!=S[h]:
                    break
                l-=1
                h+=1
            return l+1,h-1
            
        maxi=0;v=[0,0]
        
        for i in range(n):
            ff,fl=get(i,i)
            sf,sl=get(i,i+1)
            if fl-ff+1>(maxi):
                maxi=fl-ff+1
                v[0]=ff
                v[1]=fl
            if sl-sf+1>(maxi):
                maxi=sl-sf+1
                v[0]=sf
                v[1]=sl
        return S[v[0]:v[1]+1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends