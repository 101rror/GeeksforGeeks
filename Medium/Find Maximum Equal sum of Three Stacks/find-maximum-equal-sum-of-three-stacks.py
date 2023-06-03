from typing import List

class Solution:
    def maxEqualSum(self, N1:int,N2:int,N3:int, S1 : List[int], S2 : List[int], S3 : List[int]) -> int:
        s = set()
        c = 0
        
        for i in range(N1 - 1, -1, -1):
            c += S1[i]
            s.add(c)
            
        c1 = 0; new = set()
        
        for j in range(N2 - 1, -1, -1):
            c1 += S2[j]
            
            if (c1 in s):
                new.add(c1)
                
        final = set(); c2 = 0
        
        for j in range(N3 - 1, -1, -1):
            c2 += S3[j]
            if (c2 in new):
                final.add(c2)
                
        if final:
            return max(final)
            
        else:
            return 0
            
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
        
        a=IntArray().Input(3)
        
        
        S1=IntArray().Input(a[0])
        
        
        S2=IntArray().Input(a[1])
        
        
        S3=IntArray().Input(a[2])
        
        obj = Solution()
        res = obj.maxEqualSum(a[0],a[1],a[2], S1, S2, S3)
        
        print(res)
        

# } Driver Code Ends