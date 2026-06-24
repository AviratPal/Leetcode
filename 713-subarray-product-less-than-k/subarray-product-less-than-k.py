class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k<=1:
            return 0
        product=1
        left=0
        count=0
        for i in range(len(nums)):
            product=product*nums[i]

            while(product>=k):
                product=product/nums[left]
                left+=1
            count+=i-left+1
        return count        



    
        