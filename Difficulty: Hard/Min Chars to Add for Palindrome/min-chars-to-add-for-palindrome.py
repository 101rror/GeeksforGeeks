class Solution:
    def minChar(self, s):
        rev = s[::-1]
        comb = s + "#" + rev
        n = len(comb)
        dp = [0] * n
        
        for i in range(1, n):
            j = dp[i - 1]
            while j > 0 and comb[i] != comb[j]:
                j = dp[j - 1]
            if comb[i] == comb[j]:
                j += 1
            dp[i] = j
        
        return len(s) - dp[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends