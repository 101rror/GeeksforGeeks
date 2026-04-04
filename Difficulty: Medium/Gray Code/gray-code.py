class Solution:
    def graycode(self,n):
        if n == 1:
            return ['0', '1']
            
        last = self.graycode(n-1)
        ans = []
        
        for i in range(len(last)):
            ans.append('0' + last[i])
            
        for i in range(len(last)-1, -1, -1):
            ans.append('1' + last[i])
     
        return ans