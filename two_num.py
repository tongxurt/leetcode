class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for first in nums:
            for sec in nums[nums.index(first) + 1:]:
                if first + sec == target:
                    return [nums.index(first), nums[nums.index(first) + 1:].index(sec) + nums.index(first)+1]

        return []


s = Solution()
print s.twoSum([3, 3], 6)
