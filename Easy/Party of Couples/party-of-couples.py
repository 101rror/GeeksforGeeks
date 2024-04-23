from collections import defaultdict 

class Solution:
    def findSingle(self, n, arr):
        mp = defaultdict(int)
        
        for i in arr:
            mp[i] += 1
            
        for i, j in mp.items():
            if j % 2 == 1:
                return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.findSingle(N, arr))

# } Driver Code Ends