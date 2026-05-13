class Solution(object):
    def lengthOfLastWord(self, s):
        b=s.split()
        last_word=b[-1]
        return len(last_word)
        