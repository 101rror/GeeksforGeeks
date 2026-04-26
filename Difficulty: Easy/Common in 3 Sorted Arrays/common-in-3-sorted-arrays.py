class Solution:
    def commonElements(self, a, b, c):
        sta, stb, stc = set(a), set(b), set(c)
        
        return sorted(list(sta & stb & stc))