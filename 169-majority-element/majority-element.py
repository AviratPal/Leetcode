class Solution(object):
    def majorityElement(self, nums):
        frequency={}
        for i in nums:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        sorted_frequency=sorted(frequency,key=frequency.get,reverse=True)
        return sorted_frequency[0]           
       
        