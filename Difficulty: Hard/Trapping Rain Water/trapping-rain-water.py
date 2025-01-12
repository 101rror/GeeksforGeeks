
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        left = [0] * n
        right = [0] * n
        
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], arr[i])
            
        right[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], arr[i])
            
        total = 0
        for i in range(n):
            total += min(left[i], right[i]) - arr[i]
                
        return total
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