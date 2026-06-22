class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        frequency={}
        for i in s1:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        k=len(s1)
        window={}
        for i in range(k):
            if s2[i] in window:
                window[s2[i]]+=1
            else:
                window[s2[i]]=1
        if frequency==window:
            return True   
        for i in range(k,len(s2)):
            if s2[i] in window:
                window[s2[i]]+=1
            else:
                window[s2[i]]=1
            old_char=s2[i-k]
            window[old_char]-=1
            if window[old_char]==0:
                del window[old_char]
            if window==frequency:
                return True    
        return False                




        
       
        


        