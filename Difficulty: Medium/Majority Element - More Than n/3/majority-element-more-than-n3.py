class Solution:
    def findMajority(self, arr):
        n = len(arr)
        store = {}
        size = n/3
        res = []
    
        for num in arr:
            if num not in store:
                store[num] = 1
            else:
                store[num] += 1
    
            if store[num] > size:
                res.append(num)
    
        ans = list(set(res))
        ans.sort()
        
        return ans