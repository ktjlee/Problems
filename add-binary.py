# https://leetcode.com/problems/add-binary/submissions/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = self.binaryToInt(a) + self.binaryToInt(b)
        return self.intToBinary(result)
    
    def binaryToInt(self,numberString):
        result = 0
        for i in range(len(numberString)):
            if numberString[i] == "1":
                result += 2**(len(numberString)-1-i)
        return result
    
    def intToBinary(self,number):
        b = []
        if number == 0:
            return "0"
        while number > 0:
            d = number % 2
            b.append(d)
            number = number // 2
        b.reverse()
        return self.getString(b)
    
    def getString(self,l):
        result = ""
        for integer in l:
            result += str(integer)
        return result
            