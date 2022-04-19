# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        place = 0
        prevnum = nums[0]
        for i in range(1,len(nums)):
            thisnum = nums[i]
            if thisnum != prevnum:
                place += 1
                nums[place] = thisnum
                prevnum = thisnum
        return place+1
    