class Solution(object):
    def totalFruit(self, fruits):
        max_length=0
        left=0
        frequency={}
        for right in range(len(fruits)):
            if fruits[right] in frequency:
                frequency[fruits[right]]+=1
            else:
                frequency[fruits[right]]=1
            while len(frequency)>2:
                frequency[fruits[left]]-=1
                if  frequency[fruits[left]]==0:
                    del frequency[fruits[left]]
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length    





 
        