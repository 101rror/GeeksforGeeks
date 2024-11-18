#User function Template for python3

class Solution:
    
    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n
        
        self.reverse(arr, 0, d - 1)
        self.reverse(arr, d, n - 1)
        self.reverse(arr, 0, n - 1)
            
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends