class Solution:
    def findMean(self, arr, queries):
        n = len(arr)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        ans = []
        
        for querie in queries:
            x, y = querie[0], querie[1]
            tsum = prefix[y + 1] - prefix[x]
            num = y - x + 1
            
            ans.append(tsum // num)
            
        return ans
            