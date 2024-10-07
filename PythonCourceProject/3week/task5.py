"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/single-element-in-a-sorted-array/?envType=problem-list-v2&envId=array
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]