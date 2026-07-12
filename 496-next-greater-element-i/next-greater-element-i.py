class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            stack.append(num)
        ans = []
        for num in nums1:
            ans.append(next_greater[num])
        return ans   

      


