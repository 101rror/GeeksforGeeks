class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        dif = stalls[-1] - stalls[0]
        first, last = 1, dif
        
        while first <= last:
            mid = (first + last) // 2
            
            pre, count = float("-inf"), 0
            
            for stall in stalls:
                if stall - pre >= mid:
                    count += 1
                    pre = stall
                    
            if count >= k:
                first = mid + 1
            else:
                last = mid - 1
                
        return last

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends