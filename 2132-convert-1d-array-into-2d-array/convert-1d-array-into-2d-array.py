class Solution(object):
    def construct2DArray(self, original, m, n):
        if len(original)!=m*n:
            return []
        ans=[]
        temp=[]
        for i in range(len(original)):
            temp.append(original[i])
            if len(temp)==n:
                ans.append(temp)
                temp=[]
        return ans         
       
        