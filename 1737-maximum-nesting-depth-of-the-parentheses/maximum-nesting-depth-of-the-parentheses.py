class Solution(object):
    def maxDepth(self, s):
        depth=0
        maximum=0
        for i in s:
            if i=="(":
                depth+=1
                maximum=max(depth,maximum)
            elif i==")":
                depth-=1
        return maximum            
      

      
        