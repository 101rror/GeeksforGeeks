class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
     def leaders(self, A, N):
        ans = []
        mx = float('-inf')
        
        for i in range(N - 1, -1, -1):
            if(A[i] >= mx):
                mx = A[i]
                ans.append(mx)
            
        return ans[::-1]
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends