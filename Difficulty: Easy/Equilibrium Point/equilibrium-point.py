# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        totalsum = sum(arr)
        leftsum = 0
        
        for idx, num in enumerate(arr):
            totalsum -= num
            
            if leftsum == totalsum:
                return idx
                
            leftsum += num
                
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends