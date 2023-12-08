#User function Template for python3



class Solution:
    def minNumber(self, arr,n):
        def isprime(num):
            for i in range(2, int(num**0.5) + 1):
                if(num % i == 0):
                    return False
                    
            return True
            
        tsum = sum(arr)

        if(isprime(tsum)):
            return 0
            
        i = 1
        
        while(i < tsum):
            if(isprime(tsum + i)):
                return i
                
            else:
                 i += 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends