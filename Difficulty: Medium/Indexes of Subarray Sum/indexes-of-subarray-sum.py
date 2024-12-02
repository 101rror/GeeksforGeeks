#User function Template for python3
class Solution:
    def subArraySum(self, arr, target):
        n = len(arr)
        i = 0
        j = 0 
        tsum = 0
        
        if(target == 0):
            return [-1]
            
        while(j < n):
            tsum += arr[j]
            
            if(tsum > target):
                while(tsum > target):
                    tsum -= arr[i]
                    i += 1
                    
            if(tsum == target):
                return(i + 1, j + 1)
            j += 1
            
        return[-1]



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subArraySum(arr, d)
        print(" ".join(map(str,
                           result)))  # Print the result in the desired format
        tc -= 1
        print("~")

# } Driver Code Ends