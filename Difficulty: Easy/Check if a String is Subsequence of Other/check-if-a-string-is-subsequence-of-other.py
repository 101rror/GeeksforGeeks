class Solution:
    def isSubSeq(self, s1, s2):
        left, right = 0, 0
        
        while left < len(s1) and right < len(s2):
            if s1[left] == s2[right]:
                left += 1
                right += 1
            else:
                right += 1
        
        return left == len(s1)
        