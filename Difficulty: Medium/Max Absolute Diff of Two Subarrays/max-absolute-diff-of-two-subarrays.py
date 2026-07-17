class Solution:
    def maxDiffSubArrays(self, arr):
        n = len(arr)
        suffMin = [0] * (n + 1)
        suffMax = [0] * (n + 1)
        
        for i in reversed(range(n)):
            suffMin[i] = min(suffMin[i + 1] + arr[i], arr[i])
            suffMax[i] = max(suffMax[i + 1] + arr[i], arr[i])
            
        diff = abs(arr[0] - arr[1])
        prefMin = prefMax = arr[0]
        
        for i in range(1, n):
            diff = max(diff, prefMax - suffMin[i], suffMax[i] - prefMin)
            prefMin = min(prefMin + arr[i], arr[i])
            prefMax = max(prefMax + arr[i], arr[i])
            
        return diff
        