# https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        numberOfOccurances = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # Now move occurance to the beginning of the array
                nums[numberOfOccurances] = nums[i]
                # Occurance found
                numberOfOccurances += 1

        return numberOfOccurances
