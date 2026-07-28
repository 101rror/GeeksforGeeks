from collections import deque

class Solution:
    def shortestPath(self, V: int, src: int, dest: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(V)]
        
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        dists = [2 * V] * V
        q = deque([(False, src)])
        dists[src] = 0
        curr = 0
        
        while q:
            for _ in range(len(q)):
                delay, u = q.popleft()
                if delay:
                    if dists[u] > curr:
                        q.append((False, u))
                    continue
                
                if u == dest:
                    return curr
                    
                for v, w in adj[u]:
                    if dists[v] <= curr + w:
                        continue
                    dists[v] = curr + w
                    q.append((w == 2, v))
                    
            curr += 1
            
        return -1
        