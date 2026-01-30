class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2
        
        q1, q2 = deque(), deque()
        
        for _ in range(half):
            q1.append(q.popleft())
        for _ in range(half):
            q2.append(q.popleft())
            

        while q1 and q2:
            q.append(q1.popleft())
            q.append(q2.popleft())
        
        return q