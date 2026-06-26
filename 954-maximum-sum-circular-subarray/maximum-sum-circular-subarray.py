class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total_sum=sum(nums)
        current_max=nums[0]
        max_sum=nums[0]
        current_min=nums[0]
        min_sum=nums[0]
        n=len(nums)
        for i in range(1,n):
             current_max=max(nums[i],current_max+nums[i])
             max_sum=max(current_max,max_sum)
             current_min=min(nums[i],current_min+nums[i])
             min_sum=min(current_min,min_sum)
        if max_sum<0:
            return max_sum
        return max(max_sum,total_sum-min_sum)    
        
           
        
       
       
        
   
    
         
    
                    
            

       
        