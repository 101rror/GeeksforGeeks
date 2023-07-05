from typing import List

class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        l = m = 0
        r = 1
        
        while(r < n):
            cur = (prices[r] - prices[l])
            if(prices[r] > prices[l]):
                m += cur
                
            l = r
            r += 1
            
        return m

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
        
        
        prices=IntArray().Input(n)
        
        obj = Solution()
        res = obj.stockBuyAndSell(n, prices)
        
        print(res)
        

# } Driver Code Ends