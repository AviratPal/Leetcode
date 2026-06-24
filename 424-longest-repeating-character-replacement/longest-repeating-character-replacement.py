class Solution(object):
    def characterReplacement(self, s, k):
        frequency={}
        max_frequency=0
        maximum=0
        left=0
        for right in range(len(s)):
            if s[right] in frequency:
                frequency[s[right]]+=1
            else:
                frequency[s[right]]=1
            if frequency[s[right]]>max_frequency:
                max_frequency=frequency[s[right]]
            while(right-left+1)-max_frequency>k:
                frequency[s[left]]-=1
                left+=1
            maximum=max(maximum,right-left+1)
        return maximum                    
                     
  
            

   
        