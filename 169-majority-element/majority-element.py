class Solution(object):
    def majorityElement(self, nums):
        candidate=None
        count=0
        for i in nums:
            if count==0:
                candidate=i
                count=1
            elif i==candidate:
                count+=1
            else:
                count-=1
        return candidate                
        
                  
       
        