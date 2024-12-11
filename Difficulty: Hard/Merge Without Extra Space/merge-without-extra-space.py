from bisect import insort

class Solution:
    def mergeArrays(self, a, b):
        i, j = 0, 0
        n, m = len(a), len(b)
        
        while i < n and j < m:
            if a[i] <= b[j]:
                i += 1
            else:
                a[i], b[j] = b[j], a[i]
                i += 1
                
                insort(b, b.pop(j))
                    


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends