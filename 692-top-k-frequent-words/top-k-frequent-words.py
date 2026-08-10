class Solution(object):
    def topKFrequent(self, words, k):
        frequency={}
        for i in words:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        result=sorted(frequency,key=lambda x:(-frequency[x],x))
        return result[:k]        

        