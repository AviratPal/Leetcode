from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        queue=deque()
        visited=[0]*n
        queue.append(source)
        visited[source]=1
        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            for neighbour in adj[node]:
                if visited[neighbour]==0:
                    queue.append(neighbour)
                    visited[neighbour]=1
        return False        

        
       
        