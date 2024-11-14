#User function Template for python3

import heapq

class Solution:
    def nearlySorted(self, arr, k):
        n = len(arr)
        hp = []
        idx = 0
        
        for i in range(n):
            heapq.heappush(hp, arr[i])
            
            if len(hp) > k:
                arr[idx] = heapq.heappop(hp)
                idx += 1
                
        while hp:
            arr[idx] = heapq.heappop(hp)
            idx += 1





#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        print("~")
        t -= 1
# } Driver Code Ends