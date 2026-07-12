class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        next_greater={}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                next_greater[nums2[i]]=stack[-1]
            else:
                next_greater[nums2[i]]=-1
            stack.append(nums2[i])
        ans=[]
        for i in nums1:
            ans.append(next_greater[i])
        return ans                    

  

      


