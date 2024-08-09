#User function Template for python3

class Solution:
    def Maximize(self, arr): 
        mod = 10 ** 9 + 7
        arr.sort()
        tsum = 0
        
        for i in range(len(arr)):
            x = arr[i] * i
            tsum += x
            
        return tsum % mod
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends