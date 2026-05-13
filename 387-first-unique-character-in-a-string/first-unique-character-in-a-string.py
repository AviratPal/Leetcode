class Solution(object):
    def firstUniqChar(self, s):
        unique_char={}
        for i in s:
            if i in unique_char:
                unique_char[i]+=1
            else:
                unique_char[i]=1
        for i in range(len(s)):
            if unique_char[s[i]]==1:
                return i
        return -1                        
         
     
        