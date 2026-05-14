class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        x=str(abs(x))
        x=list(x)
        left=0
        right=len(x)-1
        while left<right:
            x[left],x[right]=x[right],x[left]
            left+=1
            right-=1
        result=int("".join(x))  
        result=sign*result 
        if result<-2**31 or result> 2**31 - 1:
            return 0
        else:
            return result    
     
        