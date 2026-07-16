class Solution(object):
    def longestPalindrome(self, s):
        frequency={}
        for i in s:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        length=0
        odd=False        
        for i in frequency.values():
            if i%2==0:
                length+=i
            else:
                length+=i-1
                odd=True
        if odd:
            length+=1
        return length                            
      