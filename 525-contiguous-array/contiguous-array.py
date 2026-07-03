class Solution(object):
    def findMaxLength(self, nums):
        prefix_sum=0
        first_index={0:-1}
        maximum=0
        for i in range(len(nums)):
            if nums[i]==0:
                prefix_sum-=1
            else:
                prefix_sum+=1
            if prefix_sum in first_index:
                length=i-first_index[prefix_sum]
                if length>maximum:
                    maximum=length    
            else:
                first_index[prefix_sum]=i  
        return maximum          

        
     