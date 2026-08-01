class Solution(object):
    def searchMatrix(self, matrix, target):
        rows=len(matrix)
        columns=len(matrix[0])
        low=0
        high=rows*columns-1
        while low<=high:
            mid=(low+high)//2
            row=mid//columns
            cols=mid%columns
            if matrix[row][cols]==target:
                return True
            elif matrix[row][cols]<target:
                low=mid+1
            else:
                high=mid-1
        return False                
        
            

    
        
        