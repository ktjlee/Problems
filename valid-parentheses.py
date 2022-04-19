# https://leetcode.com/problems/valid-parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = "({[()[]{})()})"
        
        stack = []
        match = {"(":")","{":"}","[":"]"}
        for i in range(len(s)):
            if s[i] == "(" or  s[i] == "{" or  s[i] == "[":
                stack.append(s[i])
            else: 
                if len(stack) == 0:
                    return False
                topofstack = stack.pop()
                if match[topofstack] != s[i]:
                    return False
        return len(stack) == 0