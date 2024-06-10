#User function Template for python3

class Solution:
	def countOddEven(self, arr, n):
		even = 0
		odd = 0
		
		for i in arr:
		    if i & 1:
		        odd += 1
		    else:
		        even += 1
		        
	    return odd, even


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    # Testcase input
    testcase = int(input())

    for _ in range(testcase):
        n = int(input())

        arr = list(map(int, input().split()))

        # Creating an object of the Solution class
        ob = Solution()

        # Calling the function to count even and odd
        res = ob.countOddEven(arr, n)

        # Printing the result
        print(*res)

# } Driver Code Ends