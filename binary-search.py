class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)-1
        while low <= high:
            middle = low + (high-low)//2
            if target < nums[middle]:
                high = middle-1
            elif target > nums[middle]:
                low = middle+1
            else: 
                return middle
            
        return -1
        