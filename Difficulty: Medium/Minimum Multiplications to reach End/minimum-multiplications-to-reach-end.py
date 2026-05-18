from collections import deque

class Solution:
    def minSteps(self, arr, start, end):
        if start == end:
            return 0
            
        MOD = 1000
        visited = [False] * MOD
        visited[start] = True
        q = deque([start])
        count = 1
        
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                for a in arr:
                    j = (i * a) % MOD
                    
                    if visited[j]:
                        continue
                    visited[j] = True
                    
                    if j == end:
                        return count
                    q.append(j)
                    
            count += 1
            
        return -1
