class Solution:
    def checkTriplet(self,arr, n):
        st = set([x*x for x in arr])
        mx = max(st)
        
        for i in st:
            for j in st:
                if i == j or i + j > mx:
                    continue
                if i + j in st:
                    return True
                    
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends