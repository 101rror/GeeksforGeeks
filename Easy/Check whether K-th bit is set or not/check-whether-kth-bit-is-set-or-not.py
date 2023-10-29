#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3


class Solution:
    def checkKthBit(self, n,k):
        if(n & (1 << k) != 0):
            return True
        else:
            return False
        
        
        

#{ 
 # Driver Code Starts.


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        obj = Solution()
        if obj.checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends