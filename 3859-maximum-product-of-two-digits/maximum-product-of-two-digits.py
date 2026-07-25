class Solution(object):
    def maxProduct(self, n):
        first=0
        second=0
        for i in str(n):
            digit=int(i)
            if digit>first:
                second =first
                first=digit
            elif digit>second: 
                second=digit
        return int(first*second)                
        
        