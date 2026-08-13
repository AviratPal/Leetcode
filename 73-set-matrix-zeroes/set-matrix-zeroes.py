class Solution(object):
    def setZeroes(self, matrix):
        rows=len(matrix)
        columns=len(matrix[0])
        zero_rows=set()
        zero_column=set()
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j]==0:
                    zero_rows.add(i)
                    zero_column.add(j)
        for i in range(rows):
            for j in range(columns):
                if i in zero_rows or j in zero_column:
                    matrix[i][j]=0
        return matrix                        
                    
                    
       