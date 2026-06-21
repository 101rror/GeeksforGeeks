class Solution:
    def chooseSwap(self, s):
        first = [-1] * 26
        
        for idx, c in enumerate(s):
            i = ord(c) - 97
            
            if first[i] == -1:
                first[i] = idx
        
        for idx in range(25):
            if first[idx] == -1:
                continue
            
            idy = idx
            
            for i in range(idx + 1, 26):
                if first[i] == -1:
                    continue
                
                idy = min(idy, i, key = lambda x: first[x])
            
            if first[idx] > first[idy]:
                c1, c2 = chr(idx + 97), chr(idy + 97)
                
                return s.translate(str.maketrans({c1: c2, c2: c1}))
        
        return s
        