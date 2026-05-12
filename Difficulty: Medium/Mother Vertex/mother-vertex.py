class Solution:
    def findMotherVertex(self, V, edges):

        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)

        def dfs(u, visited):
            visited[u] = True

            for v in adj[u]:
                if not visited[v]:
                    dfs(v, visited)

        visited = [False] * V
        x = -1

        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                x = i

        visited = [False] * V
        dfs(x, visited)

        if not all(visited):
            return -1

        for i in range(x + 1):
            visited = [False] * V
            dfs(i, visited)

            if all(visited):
                return i

        return x
        