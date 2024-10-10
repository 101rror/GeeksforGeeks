class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        n = len(arr)
        maxdist = 0
        dct = {}
        
        for i in range(n):
            if arr[i] not in dct:
                dct[arr[i]] = [i]
            else:
                dct[arr[i]].append((i))
                
        for num in dct:
            x = dct[num][-1] - dct[num][0]
            maxdist = max(maxdist, x)
            
        return maxdist



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends