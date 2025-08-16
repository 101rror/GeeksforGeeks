class Solution:
	def findLargest(self, arr):
	    newA = list(map(str, arr))
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        ans = ''.join(sorted(newA, key = cmp_to_key(compare)))
        
        if ans[0] != '0':
            return ans
        else:
            return "0"
	    