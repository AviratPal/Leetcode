class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        prefix_sum=0
        prefix_count={0:1}
        count=0
        for i in nums:
            prefix_sum+=i
            if (prefix_sum-goal) in prefix_count:
                count+=prefix_count[prefix_sum-goal]
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum]+=1
            else:
                prefix_count[prefix_sum]=1
        return count                
      
        