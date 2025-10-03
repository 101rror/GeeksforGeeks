from itertools import product
class Solution:
    def possibleWords(self, arr):
        d = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
        rep = [d[num] for num in arr if num in d]
        ans = [''.join(p) for p in product(*rep)]
        
        return ans