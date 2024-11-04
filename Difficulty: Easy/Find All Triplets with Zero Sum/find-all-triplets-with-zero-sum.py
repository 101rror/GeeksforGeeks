#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        ans = []
        d = dict()
        
        for idx, item in enumerate(arr):
            d[item] = d.get(item, [])
            d[item].append(idx)
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                ssum = arr[i] + arr[j]
                
                for k in d.get(-ssum, []):
                    if k > i and k > j:
                        ans.append(sorted([i, j, k]))
        
        
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