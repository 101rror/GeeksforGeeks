class Solution:
    def alternateSort(self,arr):
        n = len(arr)
        arr.sort()
        ans = []
        i, j = 0, n - 1
        
        while i < j:
            ans.append(arr[j])
            ans.append(arr[i])
            i += 1
            j -= 1
        
        if n % 2 != 0:
            ans.append(arr[j])
            
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends