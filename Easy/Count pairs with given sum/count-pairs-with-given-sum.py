#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        arr = sorted(arr)
        st = {}
        
        for i in arr:
            if i in st:
                st[i] += 1
            else:
                st[i] = 1
                
        count = 0
        
        for i in st:
            if(k - i in st):
                if((k - i) == i):
                    count += st[i] * (st[i] - 1)
                else:
                    count += st[i] * st[k - i]
                    
        ans = (count // 2)
                    
        return ans
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends