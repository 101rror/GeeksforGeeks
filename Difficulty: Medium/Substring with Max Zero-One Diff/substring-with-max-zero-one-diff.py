class Solution:
	def maxSubstring(self, s):
	    n = len(s)
		ans, sm = -1, 0
		
		for i in range(n):
		    sm += (-1 if s[i] == '1' else 1)
		    sm = max(0, sm)
		    ans = max(ans, sm)
		
		return ans if ans != 0 else -1
		