class Solution:
    def pairWithMaxSum(self, arr):
        def maxsubarraysum(arr):
            n = len(arr)
            ans = []
            
            for i in range(n):
                sub = arr[i : i + 2]
                ans.append(sum(sub))
                
            return ans
                
        return max(maxsubarraysum(arr)) if len(arr) >= 2 else -1


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends