class Solution(object):
    def maxProduct(self, nums):
        min_current=nums[0]
        min_product=nums[0]
        max_product=nums[0]
        max_current=nums[0]
        for i in range(1,len(nums)):
            temp=max_current
            max_current=max(nums[i],nums[i]*max_current,nums[i]*min_current)
            min_current=min(nums[i],nums[i]*temp,nums[i]*min_current)
            max_product=max(max_product,max_current)    
        return max_product       