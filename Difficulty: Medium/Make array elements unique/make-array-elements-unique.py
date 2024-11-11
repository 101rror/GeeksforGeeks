#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        n = len(arr)
        arr.sort()
        
        count = 0
        
        for i in range(1, n):
            if arr[i] <= arr[i - 1]:
                count += (arr[i - 1] + 1 - arr[i])
                arr[i] = arr[i - 1] + 1
                
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends