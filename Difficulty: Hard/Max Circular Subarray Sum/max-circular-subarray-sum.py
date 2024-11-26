#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    def kadane():
        ans = -math.inf
        cursum = 0
        
        for i in arr:
            cursum += i
            ans = max(ans, cursum)
            if cursum < 0:
                cursum = 0
        
        return ans

    def findMiniSum():
        ans = math.inf
        cursum = 0
        
        for i in arr:
            cursum += i
            ans = min(ans, cursum)
            if cursum > 0:
                cursum = 0
        
        return ans

    ans1 = kadane()
    ans2 = sum(arr) - findMiniSum()

    return max(ans1, ans2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends