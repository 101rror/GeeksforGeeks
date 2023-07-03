#User function Template for python3
class Solution:
	def maxIndexDiff(self,arr,n):
		first = 0
		last = n - 1
		curr=0
		maxi=0
		lst = list(arr)
		lst.sort()
		k =- 1
		
		while(last > first):
		    if arr[last] >= arr[first]:
		        curr = last - first
		        maxi = max(curr,maxi)
		        first += 1
		        last = n - 1
		        
		    elif(arr[first] == lst[k]):
		        first += 1
		        k -= 1
		      
		    else:
		        last -= 1
	
		return maxi

#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends