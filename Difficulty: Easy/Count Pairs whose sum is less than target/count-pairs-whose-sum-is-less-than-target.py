#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        count = 0
        left, right = 0, len(arr) - 1
        
        while left < right:
            if arr[left] + arr[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        
        return count
            

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends