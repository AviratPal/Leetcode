class Solution(object):
    def subtractProductAndSum(self, n):
        sum=0
        product=1
        for i in str(n):
            digit=int(i)
            sum+=int(i)
            product*=int(i)
        return(product-sum)    
        
       