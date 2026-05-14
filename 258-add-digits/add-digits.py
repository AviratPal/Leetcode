class Solution(object):
    def addDigits(self, num):
        while num>=10:
            count=0
            for i in str(num):
                count+=int(i)
            num=count
        return num        
     
       
        