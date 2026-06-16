class Solution(object):
    def sortedSquares(self, nums):
        result=[]
        for i in nums:
            result.append(i**2)
        result.sort()    
        return result    


        