class Solution:
    def largestSwap(self, s):
        n = len(s)
        arr = sorted(s, key = lambda e: -ord(e))
        for i in range(n):
            if s[i] < arr[i]:
                break
        else:
            return s
        
        j = s.rfind(arr[i])
        arr = list(s)
        arr[i], arr[j] = arr[j], arr[i]
        
        return "".join(arr)