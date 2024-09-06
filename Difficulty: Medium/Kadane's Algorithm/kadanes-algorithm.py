#User function Template for python3

class Solution:
    def maxSubArraySum(self,arr):
        ans = arr[0]
        check = 0
        
        for num in arr:
            check += num
            ans = max(ans, check)
            
            if check < 0:
                check = 0
                
        return ans

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