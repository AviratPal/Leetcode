class Solution(object):
    def luckyNumbers(self, matrix):
        rows=len(matrix)
        columns=len(matrix[0])
        row_min=[]
        column_max=[]
        result=[]
        for i in range(rows):
            row_min.append(min(matrix[i]))
        for j in range(columns):
            column=[]
            for i in range(rows):
                column.append(matrix[i][j])
            column_max.append(max(column))      
        for num in row_min:
            if num in column_max:
                result.append(num)
        return result        



        
        
        