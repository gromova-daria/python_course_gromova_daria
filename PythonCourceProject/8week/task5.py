"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        left = 0
        max_freq = 0

        for right in range(len(nums)):
            while (
                nums[right] * (right - left + 1) - sum(nums[left:right + 1]) > k * numOperations
            ):
                left += 1
            max_freq = max(max_freq, right - left + 1)

        return max_freq

