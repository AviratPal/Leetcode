class Solution(object):
    def transpose(self, matrix):
        rows=len(matrix)
        columns=len(matrix[0])
        result= [[0]*rows for _ in range(columns)]
        for i in range(rows):
            for j in range(columns):
                result[j][i]=matrix[i][j]
        return result        
        