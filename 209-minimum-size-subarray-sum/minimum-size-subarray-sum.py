class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        minimum=float('inf')
        current_sum=0
        for right in range(len(nums)):
            current_sum+=nums[right]
            while current_sum>=target:
                minimum=min(minimum,right-left+1)
                current_sum-=nums[left]
                left+=1
        if minimum==float("inf"):
            return 0
        else:
            return minimum            

        
                
                




    