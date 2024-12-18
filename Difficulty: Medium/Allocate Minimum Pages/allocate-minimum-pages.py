class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        if k > n:
            return -1
            
        def fun(arr, mid):
            stu = 1
            count = 0
            for i in range(n):
                if count + arr[i] <= mid:
                    count += arr[i]
                else:
                    stu += 1
                    count = arr[i]
                    
            return stu
            
        first , last = max(arr), sum(arr)
        res = -1
        
        while first <= last:
            mid = (first + last) // 2
            count = fun(arr, mid)
            if count > k:
                first = mid + 1
            else:
                res = mid
                last = mid - 1
                
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends