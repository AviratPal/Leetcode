class Solution(object):
    def allPathsSourceTarget(self, graph):
        path=[]
        ans=[]
        def dfs(node):
            path.append(node)
            if node==len(graph)-1:
                ans.append(path[:])
            else:
                for neighbour in graph[node]:
                    dfs(neighbour)
            path.pop()
        dfs(0)
        return ans                
        
        