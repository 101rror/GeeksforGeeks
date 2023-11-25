class Solution:
    def shuffleArray(self, arr, n):
        a = arr[0: n//2]
        b = arr[n//2: n]
        ans = []
        
        for i in range(n//2):
            ans.append(a[i])
            ans.append(b[i])
            
        arr.clear()
        
        arr[:] = ans[:]
        
        return arr
            


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends