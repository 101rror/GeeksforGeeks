class Solution:
    def maximumProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0  
            
        mn = float('inf')  
        mx = 0  

        for price in prices:
            mn = min(mn, price)
            mx = max(mx, price - mn)

        return mx
            

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends