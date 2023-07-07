#User function Template for python3

class Solution:
    
    def merge(self,arr1,arr2,n,m):
        x = (n + m)
        arr = (arr1 + arr2)
        arr = sorted(arr)
        
        arr1.clear()
        arr2.clear()
        
        for i in range(0, n):
            arr1.append(arr[i])
            
        for j in range(n, x):
            arr2.append(arr[j])
            
        return arr1
        return arr2

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends