class Solution(object):
    def secondHighest(self, s):
        first=-1
        second=-1
        for i in s:
            if i.isdigit():
                num=int(i)
                if num>first:
                    second=first
                    first=num
                elif num>second and num!=first:
                    second=num
        return second                
           
                   
       
        