class Solution(object):
    def canVisitAllRooms(self, rooms):
        from collections import deque
        n=len(rooms)
        visited = [0] * n
        queue = deque()
        queue.append(0)
        visited[0] = 1
        while queue:
            node = queue.popleft()
            for key in rooms[node]:
                if visited[key] == 0:
                    visited[key] = 1
                    queue.append(key)
        return sum(visited) == n
       
                        
                  

        


        