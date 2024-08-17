#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        ans = [left[i] * right[i] for i in range(n)]
        
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends