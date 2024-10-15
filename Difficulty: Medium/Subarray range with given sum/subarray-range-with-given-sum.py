#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

from collections import defaultdict

class Solution:
    def subArraySum(self,arr, tar):
        mp = defaultdict(int)
        mp[0] = 1
        count, currentsum = 0, 0

        for num in arr:
            currentsum += num
            
            checksum = (currentsum - tar)
            
            if checksum in mp:
                count += mp[checksum]
                
            mp[currentsum] += 1
                
        return count
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends