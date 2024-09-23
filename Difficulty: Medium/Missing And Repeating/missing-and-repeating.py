#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        n = len(arr)
        arrsum = sum(arr)
        setsum = sum(set(arr))
        tsum = (n * (n + 1)) // 2
        missing = abs(tsum - setsum)
        twice = abs(arrsum - setsum)
        
        return twice, missing



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends