#User function Template for python3

class Solution:
    def findSmallest(self, arr):
        mn = 1
        
        if mn > 1:
            return 1
            
        for num in arr:
            if num <= mn:
                mn += num
            else:
                break
            
        return mn


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findSmallest(arr)
        print(ans)


if __name__ == "__main__":
    main()

# } Driver Code Ends