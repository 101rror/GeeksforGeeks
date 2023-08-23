# User function Template for python3

class Solution:
    def equilibriumPoint(self,A, N):
        i = 0
        j = N - 1
        sum1 = A[i]
        sum2 = A[j]
        while(i < j):
            if(sum1 < sum2):
                sum1 += A[i + 1]
                i += 1
            else:
                sum2 += A[j - 1]
                j -= 1
        if(sum1 == sum2):
            return i + 1
        else:
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