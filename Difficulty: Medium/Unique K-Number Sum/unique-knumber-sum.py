from itertools import combinations

class Solution:
    def combinationSum(self, n, k):
        ans = []
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for comb in combinations(lst, k):
            if sum(comb) == n:
                ans.append(list(comb))
                
        return ans