#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        n = len(s)
        seen = set()
        left = 0
        maxlen = 0
        
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[right])
            maxlen = max(maxlen, right - left + 1)
                    
        return maxlen
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends