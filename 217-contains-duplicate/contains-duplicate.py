class Solution(object):
    def containsDuplicate(self, nums):
        frequency={}
        for i in nums:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        for i in frequency:
            if frequency[i]>=2:
                return True
            
        return False

       
        