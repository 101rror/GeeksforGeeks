#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends

from collections import defaultdict

class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        ans = []
        
        for i in range(n - 1):
            mp = defaultdict(list)
            for j in range(i + 1, n):
                target = 0 - arr[i] - arr[j]
                if target in mp:
                    for k in mp[target]:
                        ans.append((i, k, j))
                        
                mp[arr[j]].append(j)
                        
        return ans
        

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends