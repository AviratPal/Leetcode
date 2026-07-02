class Solution(object):
    def subarraySum(self, nums, k):
        prefix_count={0:1}
        count=0
        prefix_sum=0
        for i in nums:
            prefix_sum+=i
            if (prefix_sum-k) in prefix_count:
                count += prefix_count[prefix_sum-k]
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum]+=1
            else:
                prefix_count[prefix_sum]=1 
        return count               
        
  
        