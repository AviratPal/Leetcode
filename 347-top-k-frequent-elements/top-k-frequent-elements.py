class Solution(object):
    def topKFrequent(self, nums, k):
        frequency={}
        for i in nums:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        sorted_freq=sorted(frequency,key=frequency.get,reverse=True)
        return sorted_freq[:k]
                 
      
        