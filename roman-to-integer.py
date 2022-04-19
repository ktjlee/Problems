# https://leetcode.com/problems/roman-to-integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={"I":1, "V":5, "X":10,"L":50,"C":100,"D":500, "M":1000}
        out = 0
        for i in range(len(s)-1):
            if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                out -= d[s[i]]
            elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                out -= d[s[i]]
            elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                out -= d[s[i]]    
            else:
                out += d[s[i]]
        out += d[s[-1]]
        return out