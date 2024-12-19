#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        n = len(arr)
        first, last = 0, n - 1
        
        while first <= last:
            mid = (first + last) // 2
            check = arr[mid] - (mid + 1)
            if check < k:
                first = mid + 1
            else:
                last = mid - 1
                
        return first + k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends