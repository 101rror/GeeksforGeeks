#User function Template for python3

class Solution:
    def maxTripletSum (self, arr,  n) : 
        arr = sorted(arr, reverse = True)
        tsum = 0
        
        for i in range(n):
            if(i != 3):
                tsum += arr[i]
            else:
                break
            
        return tsum




#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.maxTripletSum(arr, n)
    print(res)



# } Driver Code Ends