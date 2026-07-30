class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows=len(mat)
        column=len(mat[0])
        count=0
        for i in range(rows):
            for j in range(column):
                if mat[i][j]==1:
                    row_count=0
                    for k in range(column):
                        if mat[i][k]==1:
                            row_count+=1
                    column_count=0
                    for l in range(rows):
                        if mat[l][j]==1:
                            column_count+=1
                    if row_count==1 and column_count==1:
                        count+=1
        return count
                     


                            
        