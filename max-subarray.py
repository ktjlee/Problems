# https://leetcode.com/problems/maximum-subarray/submissions/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        possSum = 0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if possSum < 0:
                possSum = 0  
            possSum += nums[i]
            if maxSum < possSum:
                maxSum = possSum
        return maxSum