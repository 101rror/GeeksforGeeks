#User function Template for python3

class Solution:
    def maxSubArraySum(self,arr):
        currsum = 0
        maxsum = float('-inf')
        
        for num in arr:
            currsum += num
            maxsum = max(maxsum, currsum)
            
            if currsum < 0:
                currsum = 0
                
        return maxsum
        
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends