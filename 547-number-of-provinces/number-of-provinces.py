from collections import deque
class Solution(object):
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        visited=[False]*n
        provinces=0
        for i in range(n):
            if not visited[i]:
                provinces+=1
                queue=deque()
                queue.append(i)
                visited[i]=True
                while queue:
                    node=queue.popleft()
                    for j in range(n):
                        if isConnected[node][j]==1 and not visited[j]:
                            visited[j]=True
                            queue.append(j)
        return provinces                    


                            
        
        
        