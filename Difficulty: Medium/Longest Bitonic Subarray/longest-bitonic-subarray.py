class Solution:
	def bitonic(self,arr):
		inc = dec = ans = 0
        pre = arr[0]
        
        for ele in arr:
            if ele == pre:
                inc += 1
                dec += 1
                ans = max(ans, inc, dec)
            elif ele > pre:
                inc += 1
                dec = 1
                ans = max(ans, inc)
            else:
                dec = max(dec, inc) + 1
                inc = 1
                ans = max(ans, dec)
                
            pre = ele
            
        return ans
		