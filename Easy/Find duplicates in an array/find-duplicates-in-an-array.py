from collections import Counter
class Solution:
    def duplicates(self, arr, n): 
        ans = []
        x = 0
        c = Counter(arr)
        
        for k, v in c.items():
            if(v > 1):
                x += 1
                ans.append(k)
                
        ans = sorted(ans)
        
        if(x == 0):
            return [-1]
        else:
            return ans

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends