class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1): #3-1 = 2
            if haystack[i:i+len(needle)] == needle: #1:2
                return i
        if len(needle) == 0:
            return 0
        elif needle == haystack:
            return 0
        elif len(haystack) < len(needle): 
            return -1 
        return -1
   