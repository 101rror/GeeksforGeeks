class Solution:  
    def findMaxSum(self,arr):
        n , stolen, notstolen = len(arr), 0, 0
        
        for i in range(n):
            maxstolen = max(stolen, notstolen + arr[i]) 
            maxnotstolen = max(stolen, notstolen)
            stolen, notstolen = maxstolen, maxnotstolen
            
        return max(stolen, notstolen)


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends