class Solution(object):
    def reverseWords(self, s):
        b=s.split()
        left=0
        right=len(b)-1
        while left<right:
            b[left],b[right]=b[right],b[left]
            left+=1
            right-=1
        return " ".join(b)    
                
        
      