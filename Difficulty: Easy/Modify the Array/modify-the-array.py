#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        n = len(arr)
        
        for i in range(1, n):
            if arr[i - 1] == arr[i]:
                arr[i - 1] *= 2
                arr[i] = 0
                
        zero = 0
                
        while 0 in arr:
            arr.remove(0)
            zero += 1
            
        for i in range(zero):
            arr.append(0)
                
                
        return arr
            


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        t -= 1


# } Driver Code Ends