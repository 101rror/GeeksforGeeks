class Solution:
    def URLify(self, s): 
        ans = ""
        
        for ch in s:
            if ch == ' ':
                ans += '%20'
            else:
                ans += ch
                
        return ans
        
