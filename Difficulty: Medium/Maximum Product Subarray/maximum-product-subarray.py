#User function Template for python3
class Solution:
	def maxProduct(self,arr):
	    currmax = arr[0]
	    currmin = arr[0]
	    maxpro = arr[0]
	    
	    for num in arr[1:]:
	        if num < 0:
	            currmax, currmin = currmin, currmax
	            
	        currmax = max(num, currmax * num)
            currmin = min(num, currmin * num)
            
            maxpro = max(maxpro, currmax)
	            
	            
	    return maxpro
	    
# 		def subarr(arr):
# 		    n = len(arr)
#             subarrays = []
            
#             for i in range(n):
#                 for j in range(i + 1, n + 1):
#                     subarrays.append(arr[i : j])
                    
#             return subarrays
            
#         def mul(arr):
#             ans = 1
#             for num in arr:
#                 ans *= num
                
#             return ans
            
#         ans = subarr(arr)
#         mx = float('-inf')
        
#         for new in ans:
#             x = mul(new)
#             mx = max(mx, x)
        
#         return mx


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends