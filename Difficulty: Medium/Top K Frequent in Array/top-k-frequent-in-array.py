class Solution:
	def topKFreq(self, arr, k):
		if not arr or not k:
            return []
            
        freq = {}
        
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
       
        freq = dict(sorted(freq.items(), key=lambda item: (item[1], item[0]),reverse = True))
        ans = list(freq.keys())[:k]
        return ans
		
		