class Solution(object):
    def sortVowels(self, s):
        vowels=[]
        for i in s:
            if i in "AEIOUaeiou":
                vowels.append(i)
        vowels.sort()
        s=list(s)
        k=0
        for i in range(len(s)):
                if s[i] in "AEIOUaeiou":
                       s[i]=vowels[k]
                       k+=1               
        return "".join(s)    
          
                          
   

        