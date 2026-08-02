class Solution(object):
    def majorityElement(self, nums):
        frequency={}
        ans=[]
        n=len(nums)
        for i in nums:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        for j in frequency:
            if frequency[j]>n//3:
                ans.append(j)    
        return ans              
        
        
       


        
    
       
        