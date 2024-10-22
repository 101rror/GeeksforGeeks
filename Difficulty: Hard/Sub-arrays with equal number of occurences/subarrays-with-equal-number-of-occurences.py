#User function Template for python3
import collections 

class Solution:
    def sameOccurrence(self, arr, x, y):
        counter = collections.Counter({0: 1})
        s, ans = 0, 0
        
        for e in arr:
            if e == x:
                s += 1
            elif e == y:
                s -= 1
                
            ans += counter[s]
            counter[s] += 1
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends