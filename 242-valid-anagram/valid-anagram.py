class Solution(object):
    def isAnagram(self, s, t):
        frequency={}
        if(len(s)!=len(t)):
            return False
        for i in s:
            if i in frequency:
                    frequency[i]+=1
            else:
                    frequency[i]=1
        for i in t:
            if(i not in frequency):
                return False
            frequency[i]-=1
            if(frequency[i]<0):
                    return False    
        return True        

                    


    
        