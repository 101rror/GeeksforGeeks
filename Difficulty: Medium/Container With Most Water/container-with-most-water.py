
class Solution: 
    def maxWater(self, arr):
        n = len(arr)
        maxamount = 0
        left, right = 0, n - 1
        
        while(left < right):
            amount = (right - left) * min(arr[left], arr[right])
            
            maxamount = max(maxamount, amount)
            
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
                    
        return maxamount
#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends