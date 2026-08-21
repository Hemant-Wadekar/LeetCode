class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 1
        right = len(nums)

        while (left < right):
            curr = nums[left - 1] + nums[right - 1]
            if curr == target :
                return [left,right]
            elif curr < target:
                left += 1
            else:
                right -= 1
