#User function Template for python3

class Solution:
    def maxSum(self,arr):
        n = len(arr)
        arr.sort()
        asum = 0
        
        for i in range(n // 2):
            asum += arr[n - i - 1] - arr[i]
            asum += arr[n - i - 1] - arr[i + 1]
            
        asum += arr[n // 2] - arr[0]
        
        return asum



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends