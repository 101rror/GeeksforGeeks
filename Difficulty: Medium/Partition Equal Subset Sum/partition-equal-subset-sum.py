class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        tsum = sum(arr)
        
        if tsum % 2 != 0:
            return False
            
        target = tsum // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]

#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends