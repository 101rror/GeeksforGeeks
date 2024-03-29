

from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        l = [(i+1,price[i]) for i in range(n)]
        l.sort(key=lambda item:item[1])
        i, count=0, 0
        
        while i<n and l[i][1]<=k:
            if k>=l[i][0]*l[i][1]:
                count+=l[i][0]
                k-=l[i][0]*l[i][1]
            else:
                count+=k//l[i][1]
                k%=l[i][1]
            i+=1
        return count
        



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
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends