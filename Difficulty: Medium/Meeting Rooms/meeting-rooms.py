#User function Template for python3
class Solution:
    def canAttend(self, arr):
        n = len(arr)
        arr.sort()
        
        start = arr[0][0]
        end = arr[0][1]
        
        for i in range(1, n):
            if arr[i][0] >= end:
                start = arr[i][0]
                end = arr[i][1]
            else:
                return False
            
        
        return True


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.canAttend(arr)
        if ans:
            print("true")
        else:
            print("false")

# } Driver Code Ends