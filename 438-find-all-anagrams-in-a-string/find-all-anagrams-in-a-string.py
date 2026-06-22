class Solution(object):
    def findAnagrams(self, s, p):
        result=[]
        if len(p)>len(s):
            return result    
        frequency={}
        for i in p:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        window={}
        k=len(p)
        for i in range(k):
            if s[i] in window:
                window[s[i]]+=1
            else:
                window[s[i]]=1
        if frequency==window:
            result.append(0)
        for i in range(k,len(s)):
            if s[i] in window:
                window[s[i]]+=1
            else:
                window[s[i]]=1
            old_char=s[i-k]
            window[old_char]-=1
            if window[old_char]==0:
                del window[old_char]
            if frequency==window:
                result.append(i-k+1)
        return result                                           

   
        