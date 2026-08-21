class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1

        while (left < right):
            curr = nums[left] + nums[right]
            if curr == target :
                return [left + 1,right + 1]
            elif curr < target:
                left += 1
            else:
                right -= 1
