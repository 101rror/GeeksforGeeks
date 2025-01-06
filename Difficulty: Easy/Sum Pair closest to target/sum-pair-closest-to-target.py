#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        n = len(arr)
        arr.sort()
        
        closepair = []
        closedif = float('inf')
        
        first, last = 0, n - 1
        
        while first < last:
            twosum = arr[first] + arr[last]
            dif = abs(twosum - target)
            
            if dif < closedif:
                closedif = dif
                closepair = [arr[first], arr[last]]
                
            
            if twosum == target:
                return [arr[first], arr[last]]
            elif twosum > target:
                last -= 1
            else:
                first += 1
                
                
        return closepair
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends