#User function Template for python3

class Solution:
    def power(self,N,R):
        mod = 1000000007
        ans = int(str(N)[:: -1])
        
        return pow(N, ans, mod)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends