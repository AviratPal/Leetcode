class Solution(object):
    def countPrimes(self, n):
        if n<2:
            return 0
        count=0
        prime=[True]*(n+1)
        prime[0]=prime[1]=False
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j]=False
        for i in range(2,n):
            if prime[i]:
                count+=1 
        return count                   
        

        