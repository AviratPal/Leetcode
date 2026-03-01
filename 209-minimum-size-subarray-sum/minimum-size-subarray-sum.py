class Solution(object):
    def minSubArrayLen(self, target, nums):
        i=0
        j=0
        Min_L=float('inf')
        sum=0
        while(j<len(nums)):
            sum+=nums[j]
            while(sum>=target):
                Min_L=min(Min_L,j-i+1)
                sum-=nums[i]
                i+=1
            j+=1
        return 0 if Min_L==float('inf') else Min_L       
                
                




    