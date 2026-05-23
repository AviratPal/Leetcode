class Solution(object):
    def maxVowels(self, s, k):
        vowels='aeiou'
        current_count=0
        for i in  range(k):
            if s[i] in vowels:
                current_count+=1
        maximum=current_count
        for i in range(k,len(s)):
            if s[i] in vowels:
                current_count+=1
            if s[i-k] in vowels:
                current_count-=1
            maximum=max(maximum,current_count)
        return maximum                    


   