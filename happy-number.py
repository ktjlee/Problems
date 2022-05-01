class Solution(object):
    def isHappy(self, n):
        s = set()
        summ = 0
        new = n
        while True:
            while new > 0:
                addition = new % 10
                summ += (addition)**2
                new = new //10
                print(summ)
            if summ == 1:
                return True
            elif summ in s:
                return False
            s.add(summ)
            new = summ
            summ = 0