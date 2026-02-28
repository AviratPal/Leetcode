class Solution(object):
    def findMaxAverage(self, nums, k):
        current_sum=0
        for i in range(0,k):
            current_sum+=nums[i]
        max=current_sum
        for i in range(1,len(nums)-k+1):
            current_sum=current_sum-nums[i-1]+nums[i+k-1]
            if current_sum>max:
                max=current_sum  
          
        
        return max/float(k)
        