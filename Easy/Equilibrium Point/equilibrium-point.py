# User function Template for python3

class Solution:
    def equilibriumPoint(self,A, N):
        first = 0
        last = sum(A)
        
        if(N == 1):
            return 1
            
        i = 0
        
        while(i < N):
            last -= A[i]
            
            if(first == last):
                return (i + 1)
                
            first += A[i]
            i += 1
            
        return -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends