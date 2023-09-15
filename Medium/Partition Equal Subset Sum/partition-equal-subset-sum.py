from functools import lru_cache
class Solution:
    def equalPartition(self, N, arr):
        s = sum(arr)
        if(s % 2):
            return 'NO'
            
        s = (s // 2)
        
        @lru_cache(None)
        def solve(i,cur):
            nonlocal s
            
            if(i == N):
                return cur == s
                
            if(cur == s):
                return True
                
            if(cur > s):
                return False
                
            return solve(i + 1, cur + arr[i]) or solve(i + 1, cur)

        if solve(0, 0):
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends