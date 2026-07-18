class Solution(object):
    def jump(self, nums):
        n = len(nums)
        target = n - 1
        jumps = 0
        
        while target > 0:
            for j in range(target):
                if j + nums[j] >= target:
                    target = j
                    jumps += 1
                    break
        return jumps            

       
        