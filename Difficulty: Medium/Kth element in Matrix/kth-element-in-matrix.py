class Solution:
    def kthSmallest(self, matrix, k):
        arr = [j for i in matrix for j in i]
        arr.sort()
        
        return arr[k-1]