# https://leetcode.com/problems/longest-common-prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        chari = 0
        if len(strs[0]) == 0: return ""
        
        while True:
            
            if chari >= len(strs[0]):
                return strs[0][0:chari]

            char = strs[0][chari] 
            for word in strs:
                if chari >= len(word) or char != word[chari]:
                    return strs[0][0:chari]
            chari += 1   
