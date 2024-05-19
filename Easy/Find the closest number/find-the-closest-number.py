
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        left, right = 0, n - 1
 
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < k:
                left = mid + 1
            else:
                right = mid
        if abs(arr[left - 1] - k) < abs(arr[left] - k):
            return arr[left - 1]  
        else:
            return arr[left]
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends