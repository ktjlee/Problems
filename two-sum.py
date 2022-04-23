class Solution(object):
    def twoSum(self, nums, target):
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] in hashTable:
                return [hashTable[nums[i]],i] #returns i and then its match in hashTable
            else:
                hashTable[target-nums[i]] = i