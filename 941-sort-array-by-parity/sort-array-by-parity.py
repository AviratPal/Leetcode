class Solution(object):
    def sortArrayByParity(self, nums):
        k=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
        return nums        



        
        