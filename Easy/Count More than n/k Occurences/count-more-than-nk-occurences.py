#User function Template for python3


class Solution:
    def countOccurence(self,arr,n,k):
        x = (n // k)
        count = 0
        mp = {}
        
        for i in arr:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1
                
        for i in mp:
            if(mp[i] > x):
                count += 1
                
        return count
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends