class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        
        prev = arr[0]
        arr[0] = arr[0] ^ arr[1]

        for i in range(1, n - 1):
            curr = arr[i]
            arr[i] = prev ^ arr[i + 1]
            prev = curr

        arr[n - 1] = prev ^ arr[n - 1]

        return arr
        