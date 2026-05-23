class Solution:
    def coin(self, arr):
        first, last = 0, len(arr) - 1
        
        while first < last:
            if arr[first] > arr[last]:
                first += 1
            else:
                last -= 1
                
        return arr[first]
        