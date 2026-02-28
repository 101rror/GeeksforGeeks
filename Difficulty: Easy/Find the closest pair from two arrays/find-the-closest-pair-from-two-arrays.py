class Solution:
    def findClosestPair(self, arr1, arr2, x):
        diff = abs(arr1[0] + arr2[0] - x)
        ans = (arr1[0], arr2[0])
        m, n = len(arr1), len(arr2)
        i, j = 0, n - 1
        
        while i < m and j >= 0:
            summ = arr1[i] + arr2[j]
            if (d := abs(summ - x)) < diff:
                diff = d
                ans = (arr1[i], arr2[j])
            if summ > x:
                j -= 1
            else:
                i += 1
                
        return ans