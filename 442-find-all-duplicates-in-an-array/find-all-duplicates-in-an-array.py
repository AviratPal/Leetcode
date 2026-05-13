class Solution(object):
    def findDuplicates(self, nums):
        frequency={}
        result=[]
        for i in nums:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        for i in frequency:
            if frequency[i]>1:
                result.append(i)
        return result        
                

                         
     
        