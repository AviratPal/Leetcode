class Solution(object):
    def checkInclusion(self, s1, s2):
        if s1 in s2:
            return True
        a=sorted(s1)
        k=len(a)
        for i in range(0,len(s2)-k+1):
            if sorted(s2[i:i+k])==a:
                return True
        return False        


        
       
        


        