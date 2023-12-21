#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minCandy(self, N, rat):
        arr = [1]*N
        
        for i in range(1, N):
            if rat[i] > rat[i - 1]:
                arr[i] = arr[i - 1] + 1
            else:
                arr[i] = 1
                j = i
                
                while j > 0 and rat[j - 1] > rat[j] and arr[j - 1] <= arr[j]:
                    arr[j - 1] = arr[j] + 1
                    j -= 1
        
        return sum(arr)
                
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ratings = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCandy(N, ratings)
        print(res)
# } Driver Code Ends