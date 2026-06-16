class Solution:
    def constructList(self, queries):
        ans = [0]
        xor = 0
        
        for qre, x in queries:
            if qre == 0:
                ans.append(x ^ xor)
            else:
                xor ^= x
                
        for i in range(len(ans)):
            ans[i] ^= xor
                
        ans.sort()
                
        return ans
        