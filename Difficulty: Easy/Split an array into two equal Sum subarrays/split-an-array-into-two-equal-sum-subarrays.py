class Solution:
    def canSplit(self, arr):
        tsum = sum(arr)
        
        if tsum % 2 != 0:
            return False
            
        check = 0
        half = tsum // 2
        
        for i in arr:
            check += i
            
            if check == half:
                return True
                
        return False


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends