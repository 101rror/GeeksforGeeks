import re

class Solution():
    def checkRedundancy(self, s):
        if re.search(r'\([a-zA-Z]{0,1}\)',s):
            return True
            
        return '((' in s and '))' in s