class Solution:
    def maxPeopleDefeated(self, p):
        x = 1
        
        while p >= x * x:
            p -= x * x
            x += 1
            
        x -= 1
            
        return x
        