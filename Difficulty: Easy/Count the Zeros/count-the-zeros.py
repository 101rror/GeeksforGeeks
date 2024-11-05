#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        return arr.count(0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr)
        print(ans)
        tc -= 1

        print("~")
# } Driver Code Ends