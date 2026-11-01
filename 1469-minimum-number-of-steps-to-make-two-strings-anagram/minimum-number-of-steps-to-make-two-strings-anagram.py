class Solution(object):
    def minSteps(self, s, t):
        count=0
        frequency={}
        for i in s:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        for i in t:
            if i in frequency and frequency[i]>0:
                frequency[i]-=1
            else:
                count+=1
        return count                        
        
       
        