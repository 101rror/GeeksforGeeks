#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def leastInterval(self, N, K, tasks):
        freq = {}
        
        for i in tasks:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
                
        
        mfreq = max(freq.values())
        
        ans = (K + 1) * (mfreq - 1)
        
        for i in freq.values():
            if mfreq == i:
                ans += 1
        
        return max(ans, N)
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        tasks = input().split()
        ob = Solution()
        res = ob.leastInterval(N, K, tasks)
        print(res)
# } Driver Code Ends