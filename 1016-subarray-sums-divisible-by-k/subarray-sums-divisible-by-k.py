class Solution(object):
    def subarraysDivByK(self, nums, k):
        count=0
        frequency={0:1}
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            remainder=prefix_sum%k
            if remainder in frequency:
                count+=frequency[remainder]
            if remainder in frequency:
                frequency[remainder]+=1
            else:
                frequency[remainder]=1
        return count                
                     
           
                
      
        