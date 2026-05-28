class Solution(object):
    def kthFactor(self, n, k):
        factor=[]
        if n<1:
            return False
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                factor.append(i)
                if i!=n//i:
                    factor.append(n//i)
        factor.sort()            
        if k>len(factor):
            return -1
        else:
            return factor[k-1]
          
        
        