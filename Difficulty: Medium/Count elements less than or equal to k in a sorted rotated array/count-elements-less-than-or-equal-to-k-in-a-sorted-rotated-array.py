class Solution:
    def countLessEqual(self, arr, x):
        count = 0

        for num in arr:
            if num <= x:
                count += 1
                
        return count
        