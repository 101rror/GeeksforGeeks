class Solution:
    def reverseQueue(self, q):
        first, last = 0, len(q) - 1
        
        while first < last:
            q[first], q[last] = q[last], q[first]
            first += 1
            last -= 1
        
        return q