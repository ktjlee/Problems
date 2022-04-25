# https://leetcode.com/problems/plus-one

class Solution(object):
    def makeListToInt(self, l):
        integer = 0
        for i,digit in enumerate(l):
            integer += digit*(10**(len(l)-1-i))
        return integer
    
    def makeIntToList(self, integer):
        l = []
        while integer > 0:
            addition = integer%10
            l.append(addition)
            integer = integer//10
        ll = []
        for i in range(len(l)):
            addition2 = l[-1-i]
            ll.append(addition2)
        return ll
    
    def plusOne(self, digits):
        realInteger = self.makeListToInt(digits)
        realInteger += 1
        realList = self.makeIntToList(realInteger)
        return realList
        
        
        