class Solution:
    def thirdLargest(self,a, n):
        a = sorted(a, reverse = True)
        ans = a[2]
        
        if(n > 3):
             return ans
        else:
            return -1


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr, n))
# } Driver Code Ends