class Solution:
    def romanToDecimal(self, s): 
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        cur, ans = 0, 0
        
        for e in s[::-1]:
            if cur <= d[e]:
                ans += d[e]
                cur = d[e]
            else:
                ans -= d[e]
        
        return ans