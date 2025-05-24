class Solution:
    def sumSubstrings(self,s):
        n = len(s)
        subSum = 0
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                subSum += int(s[i : j])
                
        return subSum