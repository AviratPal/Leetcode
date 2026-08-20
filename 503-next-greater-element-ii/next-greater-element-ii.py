class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        arr = [-1] * n
        for i in range(2 * n - 1, -1, -1):
            index = i % n
            while stack and nums[stack[-1]] <= nums[index]:
                stack.pop()
            if stack:
                arr[index] = nums[stack[-1]]
            stack.append(index)
        return arr


       