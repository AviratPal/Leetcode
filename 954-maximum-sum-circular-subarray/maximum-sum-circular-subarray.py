class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total_sum=sum(nums)
        min_current=nums[0]
        min_sum=nums[0]
        max_current=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            max_current=max(nums[i],max_current+nums[i])
            max_sum=max(max_sum,max_current)
            min_current=min(nums[i],min_current+nums[i])
            min_sum=min(min_sum,min_current)
        if max_sum<0:
            return max_sum
            
        return max(max_sum,total_sum-min_sum)    
    
         
    
                    
            

       
        