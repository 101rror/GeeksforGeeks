#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        mx = max(arr)
        se = -1
        
        for num in arr:
            if num > se and num != mx:
                se = num
                
        return se


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends