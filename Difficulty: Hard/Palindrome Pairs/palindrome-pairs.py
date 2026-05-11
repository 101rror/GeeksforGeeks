class Solution:
    def palindromePair(self, arr):
        seen = set()
        
        for word in arr:
            if word in seen:
                return True
            seen.add(word[::-1])

        for word in arr:
            for j in range(1, len(word)):
                p, s = word[:j], word[j:]
                if p in seen and s == s[::-1] or s in seen and p == p[::-1]:
                    return True
                    
        return False
        