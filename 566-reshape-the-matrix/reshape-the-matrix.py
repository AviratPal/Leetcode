class Solution(object):
    def matrixReshape(self, mat, r, c):
        rows=len(mat)
        temp=[]
        ans=[]
        columns=len(mat[0])
        if rows*columns!=r*c:
            return mat
        for i in range(rows):
            for j in range(columns):
                temp.append(mat[i][j])
                if len(temp)==c:
                    ans.append(temp)
                    temp=[]
        return ans            

       