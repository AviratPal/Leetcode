class Solution(object):
    def intersection(self, nums1, nums2):
        common_element=set(nums1) & set(nums2)
        return list(common_element)
       
        