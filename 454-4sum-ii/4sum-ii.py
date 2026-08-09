class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        frequency = {}
        for i in nums1:
            for j in nums2:
                total = i + j
                if total in frequency:
                    frequency[total] += 1
                else:
                    frequency[total] = 1
        count = 0
        for k in nums3:
            for l in nums4:
                target = -(k + l)
                if target in frequency:
                    count += frequency[target]
        return count
        