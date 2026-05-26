class Solution:
    def wifiRange(self, s, x):
        n = len(s)
        left = 0

        for i in range(n):
            if(s[i]  ==  '0'):
                  left += 1
            if(s[i] == '1'):
                left = - x
            if(left > x):
                return False

        if(left > 0):
            return False

        return True
