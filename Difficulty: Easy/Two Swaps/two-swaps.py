class Solution:
    def checkSorted(self, arr): 
        c = 0
        n = len(arr)
        a = sorted(arr)
        
        if a == arr and n < 4:
            return True
            
        if a == arr:
            return False
            
        for i in range(n):
            j = i + 1
            f = 1
            while arr[j - 1] != i + 1:
                j = arr[j - 1]
                if f:
                    f = 0
                    c += 1
                
            arr[i], arr[j - 1] = arr[j - 1], arr[i]
            
            if arr == a or c > 2:
                break
        return c == 0 or c == 2


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends