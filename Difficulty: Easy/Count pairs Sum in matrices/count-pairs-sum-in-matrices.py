class Solution:
	def countPairs(self, mat1, mat2, x):
		a = []
        b = []
        count = 0
        rows, cols = len(mat1), len(mat1[0])
        
        a = [mat1[j][i] for i in range(cols) for j in range(rows)]
        b = [mat2[j][i] for i in range(cols) for j in range(rows)]
        
        bset = set(b)
        
        for i in a:
          if (x - i) in bset:
               count += 1
               
        return count