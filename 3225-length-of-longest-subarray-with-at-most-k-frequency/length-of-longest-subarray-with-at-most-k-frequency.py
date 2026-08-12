class Solution(object):
    def maxSubarrayLength(self, nums, k):
        left=0
        longest=0
        frequency={}
        for right in range(len(nums)):
            if nums[right] in frequency:
                frequency[nums[right]]+=1
            else:
                frequency[nums[right]]=1
            while frequency[nums[right]]>k:
                outchar=nums[left]
                frequency[outchar]-=1
                if frequency[outchar]==0:
                    del frequency[outchar]    
                left+=1
            longest=max(longest,right-left+1)     
        return longest            
        
        